from fastapi import FastAPI
from rag import ask_question

app = FastAPI()

@app.post("/ask")
def ask(q: str):
    return {"answer": ask_question(q)}
