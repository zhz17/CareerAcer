from mcp.server.fastmcp import FastMCP

# initialize the FastMCP server
server = FastMCP("CareerAcer", "0.1.0")

@server.tool()
def get_version():
    """
    Returns the version of the CareerAcer package.
    """
    return server.version