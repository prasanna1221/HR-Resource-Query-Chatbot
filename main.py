# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.middleware.cors import CORSMiddleware
# from app.models import Query
# from app.rag_engine import query_chroma, ask_openai

# app = FastAPI()

# templates = Jinja2Templates(directory="app/templates")

# # Optional: Enable CORS if needed
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Or restrict to frontend origin
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/", response_class=HTMLResponse)
# async def serve_index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/chat")
# def chat_with_bot(query: Query):
#     documents = query_chroma(query.question)
#     answer = ask_openai(documents, query.question)
#     return {"response": answer}



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





# from fastapi import FastAPI, HTTPException, Request
# from pydantic import BaseModel
# from app.data_loader import load_employees
# from app.rag_engine import answer_query

# app = FastAPI(title="HR Resource Chatbot")

# # Load data once
# employee_data = load_employees()

# class ChatRequest(BaseModel):
#     query: str

# @app.post("/chat")
# async def chat(req: ChatRequest):
#     try:
#         response = answer_query(req.query, employee_data)
#         return {"response": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/employees/search")
# async def search_employees(skill: str = "", experience: int = 0):
#     filtered = [
#         e for e in employee_data
#         if skill.lower() in [s.lower() for s in e['skills']]
#         and e['experience_years'] >= experience
#     ]
#     return {"results": filtered}
