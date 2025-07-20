
# HR Resource Query Chatbot

## Overview
The HR Resource Query Chatbot is an intelligent assistant that allows HR teams or managers to query employee data and policies using natural language. It integrates Retrieval-Augmented Generation (RAG) with OpenAI's GPT-3.5 to retrieve relevant employee documents and generate human-like responses.

## Features
- 🤖 Natural language interface for querying HR data
- 🔍 Smart matching of employees based on skills, experience, and availability
- 🧠 Retrieval-Augmented Generation (RAG) using ChromaDB and OpenAI
- 🚀 FastAPI backend with Streamlit frontend
- 🌐 Deployed on Streamlit Cloud

## Architecture
- **Frontend**: Streamlit (`streamlit_app.py`) provides the user interface to input queries and view answers.
- **Backend**: FastAPI handles incoming queries, retrieves context from ChromaDB, and queries OpenAI for answers.
- **Vector Store**: ChromaDB stores employee documents as embeddings for retrieval.
- **LLM**: OpenAI's GPT-3.5 processes retrieved documents to generate answers.

```
User Query
   ↓
Streamlit Frontend
   ↓
FastAPI Endpoint `/chat`
   ↓
RAG Engine → ChromaDB → OpenAI Completion
   ↓
Response Displayed in UI
```

## Setup & Installation

1. **Clone the repository**
```
git clone https://github.com/your-username/hr-chatbot.git
cd hr-chatbot
```

2. **Create virtual environment and activate**
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Start backend (FastAPI)**
```
uvicorn app.main:app --reload
```

5. **Start frontend (Streamlit)**
```
streamlit run streamlit_app.py
```

## API Documentation

### POST /chat
**Description**: Accepts a query string and returns a relevant AI-generated response based on employee data.

**Request Body**
```json
{
  "question": "Find Python developers with 3+ years experience"
}
```

**Response**
```json
{
  "response": "Based on the employee data, the Python developers with 3+ years of experience are: ..."
}
```

## AI Development Process

- **AI Tools Used**: ChatGPT-4, GitHub Copilot
- **How AI Helped:**:
  - Generated initial FastAPI and Streamlit setup
  - Suggested prompt formats for better OpenAI completions
  - Helped with basic debugging and UI improvements
- **Manual Work Done:**:
  - Customized the RAG pipeline and document logic
  - Handled file structure, API integration, and deployment
  - Solved path issues and fine-tuned responses for better accuracy

## Technical Decisions

- **OpenAI vs Open Source**: Chose OpenAI GPT-3.5 for highest-quality completions. Could replace with local models later.
- **RAG with ChromaDB**: Lightweight and easy-to-use for document indexing.
- **FastAPI**: Minimalistic, fast, and production-ready API framework.
- **Streamlit**: Chosen for fast prototyping of frontend.

## Future Improvements

- Add authentication and role-based access
- Upload and manage employee data via UI
- Replace OpenAI with local LLM using Ollama or LM Studio
- Export responses or download insights as reports
- Improve document chunking and prompt engineering

## Sample Dataset (sample_employees.json)
```json
[
  {
    "name": "John Doe",
    "role": "Python Developer",
    "experience_years": 5,
    "skills": ["Python", "FastAPI", "Django"],
    "projects": ["Project A", "Project B"],
    "availability": "yes"
  },
  {
    "name": "Sarah Smith",
    "role": "Python Developer",
    "experience_years": 3,
    "skills": ["Python", "Flask"],
    "projects": ["Project X"],
    "availability": "no"
  }
]
```

## Demo

🟢 **Live Demo**: [HR Chatbot Deployed on Streamlit](https://hr-resource-query-chatbot-crravjaijmoskd3fuhqchc.streamlit.app/)
