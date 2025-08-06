"""
mcp_config.py
-------------
Configuration module for the AWS Pricing MCP server.

Defines the command, arguments, working directory, and environment variables
needed to launch and interact with the MCP server. Also provides helper functions
to retrieve these configuration values for use in agent/server management code.

Usage:
- Imported by pricing_agent.py for MCP server management
- Update paths and environment variables as needed for your environment
"""
import os
import platform
import shutil
from typing import Dict, Any

# Get the current working directory to find the MCP server
current_dir = os.getcwd()
mcp_server_dir = os.path.join(current_dir, "mcp", "src", "aws-pricing-mcp-server")

# Cross-platform command detection
def get_uv_command():
    """
    Get the appropriate uv command for the current platform.
    Returns:
        str: The uv command to use.
    """
    # Check if uv is available in PATH
    if shutil.which("uv"):
        return "uv"
    # Fallback to python -m uv (if installed via pip)
    elif shutil.which("python") and os.system("python -c 'import uv' 2>/dev/null") == 0:
        return "python"
    else:
        return "uv"  # Default fallback

def get_uv_args():
    """
    Get the appropriate uv arguments for the current platform.
    Returns:
        list: The uv arguments to use.
    """
    uv_cmd = get_uv_command()
    if uv_cmd == "python":
        return ["-m", "uv", "run", "awslabs.aws-pricing-mcp-server"]
    else:
        return ["run", "awslabs.aws-pricing-mcp-server"]

# MCP Server Configuration
MCP_SERVER_CONFIG = {
    "command": get_uv_command(),  # Use platform-appropriate uv command
    "args": get_uv_args(),  # Run the server script
    "cwd": mcp_server_dir,  # Set working directory to the MCP server
    "env": {
        # Add any environment variables needed for the AWS pricing server
        "AWS_REGION": os.getenv("AWS_REGION", "us-east-1"),
        "AWS_PROFILE": os.getenv("AWS_PROFILE", "default"),
        "PYTHONPATH": mcp_server_dir,  # Add the server directory to Python path
    }
}

# Available MCP Resources (these will be discovered at runtime)
MCP_RESOURCES = {
    "pricing_data": "aws-pricing-data",
    "service_catalog": "aws-service-catalog",
    "price_history": "aws-price-history"
}

# Available MCP Tools (these will be discovered at runtime)
MCP_TOOLS = {
    "get_pricing": "get-aws-pricing",
    "compare_pricing": "compare-aws-pricing",
    "search_services": "search-aws-services"
}

def get_mcp_server_path() -> str:
    """
    Get the path to the MCP server executable (usually 'uv').
    Returns:
        str: The command to run the MCP server.
    """
    return MCP_SERVER_CONFIG["command"]

def get_mcp_server_args() -> list:
    """
    Get the arguments for the MCP server (e.g., ['run', 'awslabs.aws-pricing-mcp-server']).
    Returns:
        list: Arguments for the MCP server command.
    """
    return MCP_SERVER_CONFIG["args"]

def get_mcp_server_cwd() -> str:
    """
    Get the working directory for the MCP server (where the server code lives).
    Returns:
        str: The working directory path.
    """
    return MCP_SERVER_CONFIG["cwd"]

def get_mcp_environment() -> Dict[str, str]:
    """
    Get environment variables for MCP server (region, profile, PYTHONPATH, etc).
    Returns:
        dict: Environment variables for the MCP server process.
    """
    return MCP_SERVER_CONFIG["env"] 