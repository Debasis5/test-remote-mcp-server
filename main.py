import random
from fastmcp import FastMCP
import json

#Create a FastMCP server instance
mcp = FastMCP(name = "Simple Calculator Server")

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.

    Args:
        a:first number
        b:second number

    Returns:
        The sum of a and b   
    
    """
    return a + b

@mcp.tool
def radom_number(min_val:int =1, max_val: int = 100) -> int:
    """
    Generate a random number within a range.

    Args:
        min_value: Minimum value (default:1)
        ma_value: Maximum value (default:100)

    Returns:
        A random integer between min_val and max_val
    """

    return random.randint(min_val, max_val)

#Resource: Server information
@mcp.resource("info://server")
def server_info() -> str:
    """get information about this server."""

    info = {
        "name": "Simple Calculator Server.",
        "version": "1.0.0",
        "description": "A basic MCP server with a math tool",
        "tools": ["add", "random_number"],
        "author": "Debasis"
        }

    return json.dumps(info, indent = 2)


#Start the server
if __name__ == "__main__":
    mcp.run(transport = "http", host = "0.0.0.0", port = 8000)