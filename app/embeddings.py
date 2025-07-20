import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")

def get_embedding(text: str):
    return client.embeddings.create(
        input=[text],
        model=EMBEDDING_MODEL
    ).data[0].embedding
