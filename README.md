# LLM Agent with GUI

A chat agent with a web UI. The backend is a Python FastAPI + LangChain agent that uses a local Ollama model and DuckDuckGo web search. The frontend is a Next.js app using prompt-kit components.

## Architecture

```
Browser → Next.js (port 3000) → /api/chat proxy → FastAPI (port 8000)
                                                         ↓
                                               Ollama (port 11434)
                                               DuckDuckGo search
```

## Prerequisites

- [Node.js](https://nodejs.org/) v18+
- [Python](https://python.org/) 3.10+
- [Ollama](https://ollama.com/) running locally

## Setup

### 1. Start Ollama

Make sure Ollama is running and pull the model:

```bash
ollama pull gpt-oss:120b-cloud
```

Or run the included PowerShell helper on Windows:

```powershell
.\launch-ollama.ps1
```

To use a different model, set the `OLLAMA_MODEL` environment variable before starting the backend.

### 2. Start the backend

```bash
cd python-agent
pip install -r requirements.txt
python main.py
```

The API will be available at `http://localhost:8000`.

**Environment variables (optional):**

| Variable         | Default                  | Description              |
|------------------|--------------------------|--------------------------|
| `OLLAMA_MODEL`   | `gpt-oss:120b-cloud`     | Ollama model to use      |
| `OLLAMA_BASE_URL`| `http://localhost:11434` | Ollama server URL        |

Create a `.env` file in `python-agent/` to set these.

### 3. Start the frontend

```bash
cd prompt-kit-temp
npm install
npm run dev
```

Open `http://localhost:3000` in your browser.

## Project structure

```
├── python-agent/          # FastAPI backend
│   ├── agent/
│   │   ├── api.py         # POST /chat endpoint
│   │   ├── core.py        # LangChain agent logic + DuckDuckGo search
│   │   └── config.py      # Env-based configuration
│   ├── main.py            # Uvicorn entry point
│   └── requirements.txt
│
├── prompt-kit-temp/       # Next.js frontend
│   ├── app/
│   │   ├── page.tsx       # Home → renders AgentChat
│   │   ├── api/chat/      # Proxy route to backend
│   │   └── ...
│   └── components/
│       ├── agent/         # AgentChat component
│       └── prompt-kit/    # Reusable chat UI components
│
└── launch-ollama.ps1      # Windows helper to start Ollama
```
