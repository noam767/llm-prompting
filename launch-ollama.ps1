$env:OLLAMA_VULKAN = "1"
$env:ANTHROPIC_AUTH_TOKEN = "ollama"
$env:ANTHROPIC_API_KEY = ""
$env:ANTHROPIC_BASE_URL = "http://localhost:11434"

try {
    Invoke-WebRequest -Uri "http://localhost:11434" -UseBasicParsing -TimeoutSec 3 -ErrorAction Stop | Out-Null
    Write-Host "Ollama is running." -ForegroundColor Green
} catch {
    Write-Host "ERROR: Ollama is not responding." -ForegroundColor Red
    exit 1
}

claude --model minimax-m2.5:cloud --dangerously-skip-permissions