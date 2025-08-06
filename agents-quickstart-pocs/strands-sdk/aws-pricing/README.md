# AWS Pricing Agent Chatbot

A Streamlit-based chatbot that uses Strands Agents and the AWS Pricing MCP (Model Context Protocol) server to provide intelligent responses about AWS pricing and cost analysis.

## Features

- 🤖 **AI-Powered Responses**: Uses Strands Agents for intelligent AWS pricing queries
- 🔗 **MCP Integration**: Connects to AWS Pricing MCP server for real-time pricing data
- 💬 **Chat Interface**: Multi-line input with chat history
- 🎨 **Modern UI**: Clean, AWS-branded interface with responsive design
- 🔄 **Cross-Platform**: Works on macOS, Windows, and Linux

## Prerequisites

### System Requirements
- Python 3.8 or higher
- Git
- Internet connection for downloading dependencies

### Platform-Specific Requirements

#### macOS
- Homebrew (recommended for easy installation)
- Terminal or iTerm2

#### Windows
- Windows 10 or higher
- Command Prompt or PowerShell
- Git Bash (recommended for Unix-like commands)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd aws-pricing
```

### 2. Create Virtual Environment

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install UV (Required for MCP Server)

#### macOS
```bash
# Using Homebrew
brew install uv

# Or using pip
pip install uv
```

#### Windows
```cmd
# Using pip
pip install uv

# Or download from https://github.com/astral-sh/uv/releases
```

### 5. Install AWS Pricing MCP Server

```bash
# Clone the MCP repository
git clone https://github.com/awslabs/mcp.git
cd mcp/src/aws-pricing-mcp-server

# Install dependencies
uv pip install -r uv-requirements.txt

# Return to project directory
cd ../../../aws-pricing
```

## Configuration

### AWS Credentials (Optional)

For enhanced functionality, configure AWS credentials:

#### macOS/Linux
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=us-east-1
```

#### Windows
```cmd
set AWS_ACCESS_KEY_ID=your_access_key
set AWS_SECRET_ACCESS_KEY=your_secret_key
set AWS_REGION=us-east-1
```

## Usage

### Starting the Chatbot

#### Option 1: Using the Launcher Script
```bash
python run_chatbot.py
```

#### Option 2: Direct Streamlit Command
```bash
streamlit run streamlit_chatbot.py
```

### Using the Chatbot

1. **Initialize Agent**: Click the "Initialize Agent" button in the sidebar
2. **Ask Questions**: Type your AWS pricing questions in the text area
3. **Get Responses**: The agent will provide intelligent responses based on AWS pricing knowledge

### Example Questions

- "What are the pricing differences between EC2 instance types?"
- "How does AWS pricing vary by region?"
- "What are the cost optimization strategies for S3?"
- "Compare pricing between on-demand and reserved instances"
- "What factors affect AWS pricing?"

## Project Structure

```
aws-pricing/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── pricing_agent.py         # Main agent with MCP integration
├── mcp_config.py           # MCP server configuration
├── streamlit_chatbot.py    # Streamlit web application
├── run_chatbot.py          # Launcher script
├── test_agent.py           # Testing script
└── venv/                   # Virtual environment (created during setup)
```

## Troubleshooting

### Common Issues

#### 1. "Streamlit not found" Error
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

#### 2. "UV not found" Error
**Solution**: Install UV
```bash
# macOS
brew install uv

# Windows
pip install uv
```

#### 3. "MCP server connection failed" Error
**Solution**: Ensure MCP server is properly installed
```bash
cd mcp/src/aws-pricing-mcp-server
uv pip install -r uv-requirements.txt
```

#### 4. Port Already in Use
**Solution**: Use a different port
```bash
streamlit run streamlit_chatbot.py --server.port 8502
```

### Platform-Specific Issues

#### macOS
- If you get permission errors, ensure your terminal has the necessary permissions
- For Homebrew installation issues, try `brew doctor`

#### Windows
- If Python is not found, add Python to your PATH
- For Git Bash issues, try using Command Prompt instead
- If you get SSL errors, update your certificates

## Development

### Running Tests
```bash
python test_agent.py
```

### Code Structure
- `pricing_agent.py`: Core agent logic with MCP integration
- `mcp_config.py`: Cross-platform MCP server configuration
- `streamlit_chatbot.py`: Web interface with AWS branding
- `run_chatbot.py`: Cross-platform launcher script

### Adding Features
1. Modify `pricing_agent.py` for new agent capabilities
2. Update `streamlit_chatbot.py` for UI changes
3. Test on both platforms before committing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test on both macOS and Windows
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the project structure
3. Test on both platforms
4. Open an issue with detailed information

## Acknowledgments

- [Strands Agents](https://strandsagents.com) for the AI agent framework
- [AWS Pricing MCP Server](https://github.com/awslabs/mcp/tree/main/src/aws-pricing-mcp-server) for pricing data
- [Streamlit](https://streamlit.io) for the web interface
- [UV](https://github.com/astral-sh/uv) for fast Python package management 