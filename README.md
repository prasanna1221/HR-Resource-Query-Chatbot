# HR Resource Query Chatbot

## 🧠 Overview
This is an intelligent HR assistant chatbot that answers natural language queries to help HR teams find employees based on skills, experience, and project history.

## 🚀 Features
- Natural language query interpretation (RAG system)
- Search employees by skill/experience
- Streamlit UI frontend
- FastAPI backend with OpenAI API integration

## 📐 Architecture
- FastAPI for backend API
- Streamlit for frontend
- OpenAI Embeddings + LLM for RAG
- JSON for employee data

## 🛠️ Setup & Installation
```bash
git clone https://github.com/yourrepo/hr-chatbot
cd hr-chatbot
pip install -r requirements.txt
streamlit run frontend/app.py
uvicorn app.main:app --reload
