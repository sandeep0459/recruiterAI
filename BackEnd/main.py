from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from qa_bot import get_qa_chain


#initialize FastAPI
app = FastAPI()

#load the RAG pipleine
qa_chain = get_qa_chain()

# Input structure: defines what data the user sends
class Query(BaseModel):
    question: str

# Output structure: defines what response we return
class Answer(BaseModel):
    answer: str

#Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # Allow all origins (you can restrict this)
    allow_methods=["*"],     # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],     # Allow all headers
)

# POST endpoint that accepts question and returns answer
@app.post("/ask", response_model=Answer)
async def ask_question(query: Query):
    # Run the RAG chain to get an answer from vectorstore + LLM
    response = qa_chain.run(query.question)

    # Return the answer in a structured format
    return Answer(answer=response)