@echo off
echo Starting Development AI Assistant...
echo.

REM Check if backend is running
curl -s http://localhost:8000/health >nul 2>&1
if %errorlevel% neq 0 (
    echo Backend not running. Starting backend server...
    echo.
    start "Backend Server" cmd /k "cd ..\backend && uvicorn main:app --reload --host 0.0.0.0 --port 8000"
    echo Waiting for backend to start...
    timeout /t 5 /nobreak >nul
) else (
    echo Backend is already running!
)

echo.
echo Opening Development AI Assistant...
start "" "dev-assistant.html"

echo.
echo Development AI Assistant is now running!
echo - Backend: http://localhost:8000
echo - Assistant: dev-assistant.html
echo.
echo Press any key to exit...
pause >nul
