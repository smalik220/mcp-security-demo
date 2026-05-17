import logging
from pathlib import Path

from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("mcp-secure-demo")

ALLOWED_PATHS = ["bestanden/leesbaar-bestand.md"]


@mcp.tool()
def read_file(path: str) -> str:
    """Leest een toegestaan bestand. Toegang is beperkt via een allowlist."""
    if ".." in path:
        logger.warning(f"Path traversal attempt geblokkeerd: {path}")
        return "Access denied: path traversal gedetecteerd"

    if path not in ALLOWED_PATHS:
        logger.warning(f"Access denied: {path}")
        return "Access denied: bestand staat niet op de allowlist"

    logger.info(f"Bestand gelezen: {path}")
    return Path(path).read_text()


if __name__ == "__main__":
    mcp.run()
