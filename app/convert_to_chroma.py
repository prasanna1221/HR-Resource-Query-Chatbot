import json
from pathlib import Path
from chromadb import PersistentClient
from embeddings import get_embedding

# Initialize ChromaDB persistent client
chroma_client = PersistentClient(path=str(Path(__file__).resolve().parent.parent / "chroma"))

# Get or create collection
collection = chroma_client.get_or_create_collection(name="employees")

# Load employees.json
with open(Path(__file__).resolve().parent.parent / "data/employees.json", "r") as f:
    data = json.load(f)["employees"]

# Add data to ChromaDB
for idx, record in enumerate(data):
    text = json.dumps(record)
    embedding = get_embedding(text)
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[f"emp-{idx}"]
    )

print("✅ ChromaDB collection created and saved.")
