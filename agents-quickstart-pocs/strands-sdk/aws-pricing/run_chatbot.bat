@echo off
REM AWS Pricing Agent Chatbot Launcher for Windows
REM This batch file provides an easy way to run the chatbot on Windows

echo.
echo ========================================
echo   AWS Pricing Agent Chatbot Launcher
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if requirements are installed
if not exist "venv\Lib\site-packages\streamlit" (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Check if streamlit is available
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Streamlit not found. Installing...
    pip install streamlit
)

echo.
echo Starting AWS Pricing Agent Chatbot...
echo The app will open in your browser at: http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

REM Run the chatbot
python run_chatbot.py

REM If we get here, the app was closed
echo.
echo Chatbot stopped. Press any key to exit...
pause >nul 