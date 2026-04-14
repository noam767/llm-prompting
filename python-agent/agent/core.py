from typing import Any
import asyncio

from duckduckgo_search import DDGS
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from .config import settings


def _to_lc_messages(messages: list[dict[str, str]]) -> list[Any]:
    """Convert simple role/content dictionaries to LangChain message objects.

    Args:
        messages: Conversation history where each entry has ``role`` and
            ``content`` keys.

    Returns:
        List of LangChain message instances preserving the original order.
    """

    lc_messages: list[Any] = []
    for msg in messages:
        if msg["role"] == "user":
            lc_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            lc_messages.append(AIMessage(content=msg["content"]))
        elif msg["role"] == "system":
            lc_messages.append(SystemMessage(content=msg["content"]))
    return lc_messages


async def _duckduckgo_search(query: str, max_results: int = 5) -> str:
    """Run a DuckDuckGo web search in a background thread.

    This avoids blocking the event loop while still returning a simple
    text summary of top results.
    """

    loop = asyncio.get_running_loop()

    def _search() -> str:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        lines: list[str] = []
        for item in results:
            title = item.get("title") or "Result"
            href = item.get("href") or ""
            snippet = item.get("body") or ""
            lines.append(f"- {title} ({href}) — {snippet}")
        return "\n".join(lines) if lines else "No recent web results found."

    return await loop.run_in_executor(None, _search)


async def run_agent(messages: list[dict[str, str]]) -> str:
    """Run a minimal LangChain agent backed by DuckDuckGo search.

    The agent uses DuckDuckGo to fetch recent information for the latest user
    question and passes the results, together with the chat history, to a
    local Ollama chat model.

    Args:
        messages: Full chat history including the latest user question.

    Returns:
        The assistant's answer as a plain text string.
    """

    model = ChatOllama(
        model=settings.model,
        temperature=0.2,
        base_url=settings.ollama_base_url,
    )
    history = _to_lc_messages(messages[:-1])
    latest_question = messages[-1]["content"]

    search_results = await _duckduckgo_search(latest_question, max_results=5)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "You are a helpful assistant. Use the provided web search "
                    "results to answer questions about recent years when "
                    "relevant."
                ),
            ),
            MessagesPlaceholder(variable_name="history"),
            (
                "human",
                "Question: {question}\n\nSearch results:\n{search_results}",
            ),
        ]
    )

    chain = prompt | model | StrOutputParser()

    answer = await chain.ainvoke(
        {
            "history": history,
            "question": latest_question,
            "search_results": search_results,
        }
    )
    return answer
