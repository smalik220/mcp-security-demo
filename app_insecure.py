from fastapi import FastAPI
from pathlib import Path

app = FastAPI()


@app.get("/read_file")
def read_file(path: str):
    return {"content": Path(path).read_text()}
