#!/usr/bin/env python3
"""
run_chatbot.py
--------------
Launcher script for the AWS Pricing Agent Chatbot Streamlit app.

Checks environment, dependencies, and launches the Streamlit web interface.
Provides helpful output for setup and troubleshooting.

Usage:
- Run directly: python run_chatbot.py
- Requires: streamlit_chatbot.py and all dependencies installed
"""
import subprocess
import sys
import os
import platform
import shutil

def check_streamlit():
    """
    Check if Streamlit is available in the current environment.
    Returns:
        bool: True if Streamlit is available, False otherwise.
    """
    try:
        import streamlit
        return True
    except ImportError:
        return False

def get_streamlit_command():
    """
    Get the appropriate command to run Streamlit based on the platform.
    Returns:
        list: Command list to run Streamlit.
    """
    # Try to use streamlit directly
    if shutil.which("streamlit"):
        return ["streamlit", "run", "streamlit_chatbot.py"]
    # Fallback to python -m streamlit
    else:
        return [sys.executable, "-m", "streamlit", "run", "streamlit_chatbot.py"]

def main():
    """
    Launch the Streamlit chatbot app.
    Checks for Streamlit, prints helpful info, and runs the app.
    """
    print("🚀 Starting AWS Pricing Agent Chatbot...")
    print("📝 Make sure you have:")
    print("   - Python virtual environment activated")
    print("   - Dependencies installed (pip install -r requirements.txt)")
    print("   - AWS credentials configured (optional)")
    print()
    
    # Check if streamlit is available
    if not check_streamlit():
        print("❌ Streamlit not found. Please install dependencies:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    print("✅ Streamlit is available")
    
    # Launch Streamlit app
    print("🌐 Opening chatbot in your browser...")
    print("📱 The app will be available at: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the server")
    print()
    
    try:
        # Get the appropriate command for this platform
        streamlit_cmd = get_streamlit_command()
        
        # Add platform-specific arguments
        if platform.system() == "Windows":
            # Windows-specific settings
            cmd = streamlit_cmd + [
                "--server.port", "8501",
                "--server.address", "localhost",
                "--server.headless", "true"
            ]
        else:
            # Unix-like systems (macOS, Linux)
            cmd = streamlit_cmd + [
                "--server.port", "8501",
                "--server.address", "localhost"
            ]
        
        # Run the Streamlit app
        subprocess.run(cmd)
        
    except KeyboardInterrupt:
        print("\n👋 Chatbot stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting chatbot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 