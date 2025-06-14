import os
import time
from mcp.server.fastmcp import FastMCP

# initialize the FastMCP server
server = FastMCP("CareerAcer", "0.1.0")

@server.tool()
def load_cvs(cv_path: str) -> list:
    """
    Tool to load a CV from a specified path.
    """
    if not os.path.exists(cv_path):
        return f"CV file not found at {cv_path}"
    
    return os.listdir(cv_path)
    
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

if __name__ == "__main__":
    # Initialize and run the server
    server.run(transport='stdio')