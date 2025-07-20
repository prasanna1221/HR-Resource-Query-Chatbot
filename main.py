from fastapi import FastAPI
from app.models import Query
from app.rag_engine import query_chroma, ask_openai

app = FastAPI()

@app.post("/chat")
def chat_with_bot(query: Query):
    documents = query_chroma(query.question)
    print("Retrieved documents:", documents)
    print("User query:", query.question)
    answer = ask_openai(documents, query.question)
    return {"response": answer}