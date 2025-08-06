#!/bin/bash

# AWS Pricing Agent Chatbot Launcher for macOS/Linux
# This shell script provides an easy way to run the chatbot on Unix-like systems

echo ""
echo "========================================"
echo "  AWS Pricing Agent Chatbot Launcher"
echo "========================================"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

# Check if virtual environment exists
if [ ! -f "venv/bin/activate" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if requirements are installed
if [ ! -d "venv/lib/python*/site-packages/streamlit" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
fi

# Check if streamlit is available
python -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "ERROR: Streamlit not found. Installing..."
    pip install streamlit
fi

echo ""
echo "Starting AWS Pricing Agent Chatbot..."
echo "The app will open in your browser at: http://localhost:8501"
echo "Press Ctrl+C to stop the server"
echo ""

# Run the chatbot
python run_chatbot.py

# If we get here, the app was closed
echo ""
echo "Chatbot stopped." 