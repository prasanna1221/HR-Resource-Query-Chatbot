from chromadb import Client
from chromadb.config import Settings
from openai import OpenAI
import numpy as np

client = OpenAI()

def query_chroma(query: str, top_k: int = 3):
    chroma_client = Client(Settings(
        persist_directory="chroma"
    ))
    collection = chroma_client.get_or_create_collection(name="employees")
    
    query_embedding = client.embeddings.create(
        input=[query],
        model="text-embedding-ada-002"
    ).data[0].embedding

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    documents = results['documents'][0]
    return documents

def ask_openai(context_docs, query):
    prompt = f"""
You are a helpful assistant. Use the following employee data to answer the question.

Context:
{chr(10).join(context_docs)}

Question: {query}
Answer:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
