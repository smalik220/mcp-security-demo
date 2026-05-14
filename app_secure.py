import logging

from fastapi import FastAPI, HTTPException
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

ALLOWED_PATHS = ["bestanden/leesbaar-bestand.md"]


@app.get("/read_file")
def read_file(path: str):
    if path not in ALLOWED_PATHS:
        logger.warning(f"Toegang geweigerd: {path}")
        raise HTTPException(status_code=403, detail="Toegang geweigerd")
    logger.info(f"Bestand gelezen: {path}")
    return {"content": Path(path).read_text()}
