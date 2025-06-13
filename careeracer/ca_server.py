import os
import time
from mcp.server.fastmcp import FastMCP

# initialize the FastMCP server
server = FastMCP("CareerAcer", "0.1.0")

@server.tool()
def result_storage(result: str) -> str:
    """
    Tool to store results in a file.
    """
    # Define the path to the results file
    results_file = f"results_{time.localtime()}.txt"
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(results_file), exist_ok=True)
    
    # Open the file in append mode and write a sample result
    with open(results_file, "a") as file:
        file.write(f"{result}\n")
    
    return f"Results stored in {results_file}"