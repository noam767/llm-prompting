from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .core import run_agent


class ChatMessage(BaseModel):
    """Single chat message exchanged with the agent."""

    role: Literal["user", "assistant", "system"]
    content: str


class ChatRequest(BaseModel):
    """Request body for the /chat endpoint."""

    messages: list[ChatMessage]
    stream: bool | None = False


class ChatResponse(BaseModel):
    """Simplified response containing the assistant's answer."""

    answer: str


app = FastAPI(title="LangChain Tavily Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Handle chat requests from the frontend.

    Validates the incoming message history and forwards it to the LangChain
    agent. Returns the generated answer wrapped in a Pydantic model.

    Args:
        request: Incoming chat payload including the conversation history.

    Returns:
        Response object containing the assistant answer text.

    Raises:
        HTTPException: If the request does not include any messages.
    """

    if not request.messages:
        raise HTTPException(status_code=400, detail="messages must not be empty")

    answer = await run_agent(
        [{"role": m.role, "content": m.content} for m in request.messages]
    )
    return ChatResponse(answer=answer)
