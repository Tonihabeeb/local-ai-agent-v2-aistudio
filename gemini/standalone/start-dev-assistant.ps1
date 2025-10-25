Write-Host "Starting Development AI Assistant..." -ForegroundColor Green
Write-Host ""

# Check if backend is running
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/health" -TimeoutSec 2 -ErrorAction Stop
    Write-Host "Backend is already running!" -ForegroundColor Green
} catch {
    Write-Host "Backend not running. Starting backend server..." -ForegroundColor Yellow
    Write-Host ""
    
    # Set environment variable
    $env:GEMINI_API_KEY = "AIzaSyBuBtWuWDuX0SUWW-n_xWk7QA0qLOKsWcE"
    
    # Start backend in new window
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd ..\backend; uvicorn main:app --reload --host 0.0.0.0 --port 8000"
    
    Write-Host "Waiting for backend to start..." -ForegroundColor Yellow
    Start-Sleep -Seconds 5
}

Write-Host ""
Write-Host "Opening Development AI Assistant..." -ForegroundColor Cyan

# Open the assistant
Start-Process "dev-assistant.html"

Write-Host ""
Write-Host "Development AI Assistant is now running!" -ForegroundColor Green
Write-Host "- Backend: http://localhost:8000" -ForegroundColor Cyan
Write-Host "- Assistant: dev-assistant.html" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
