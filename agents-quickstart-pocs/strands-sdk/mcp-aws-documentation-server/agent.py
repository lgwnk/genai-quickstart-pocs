from mcp import stdio_client, StdioServerParameters
from strands import Agent
from strands.tools.mcp import MCPClient
import asyncio

# Synchronous function to query AWS documentation using the agent
# Returns the full response as a string (or AgentResult)
def query_aws_docs(query_string: str):
    # Create an MCP client that launches the AWS Documentation MCP Server
    stdio_mcp_client = MCPClient(lambda: stdio_client(
        StdioServerParameters(
            command="uvx", 
            args=["awslabs.aws-documentation-mcp-server@latest"]
        )))
    # Use a synchronous context manager for MCPClient
    with stdio_mcp_client:
        tools = stdio_mcp_client.list_tools_sync()
        agent = Agent(tools=tools)
        return agent(query_string)

# Internal generator to stream agent results as strings (if supported)
def _stream_agent_chunks(query_string: str):
    # Create an MCP client for the AWS Documentation MCP Server
    stdio_mcp_client = MCPClient(lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            args=["awslabs.aws-documentation-mcp-server@latest"]
        )
    ))
    # Use a synchronous context manager for MCPClient
    with stdio_mcp_client:
        tools = stdio_mcp_client.list_tools_sync()
        agent = Agent(tools=tools)
        # If the agent supports streaming, yield each chunk as a string
        if hasattr(agent, 'stream'):
            for chunk in agent.stream(query_string):
                # Extract string content from chunk (AgentResult or similar)
                if hasattr(chunk, 'text'):
                    yield chunk.text
                elif hasattr(chunk, 'content'):
                    yield chunk.content
                else:
                    yield str(chunk)
        else:
            # Fallback: yield the full result as a string
            result = agent(query_string)
            if hasattr(result, 'text'):
                yield result.text
            elif hasattr(result, 'content'):
                yield result.content
            else:
                yield str(result)

# Async generator to stream agent results in a non-blocking way for the UI
async def query_aws_docs_streaming(query_string: str):
    loop = asyncio.get_event_loop()
    # Run the blocking streaming generator in a thread executor
    for chunk in await loop.run_in_executor(None, lambda: list(_stream_agent_chunks(query_string))):
        yield chunk

if __name__ == "__main__":
    # Example CLI usage: print the result of a sample query
    response = query_aws_docs("look up documentation on S3 bucket naming rule. cite your sources")
    print(response)
        
