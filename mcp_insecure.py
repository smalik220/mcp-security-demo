from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-insecure-demo")


@mcp.tool()
def read_file(path: str) -> str:
    """Leest een bestand op basis van het opgegeven pad."""
    return Path(path).read_text()


if __name__ == "__main__":
    mcp.run()
