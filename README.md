# RecruiterAI

**RecruiterAI** is an AI-powered recruitment assistant that allows users to interact with resumes in a conversational format. The project consists of a Python-based backend for document ingestion and question answering, and a React-based frontend interface for user interaction.

---

## 🌐 Features

- Upload and parse resumes
- Ask natural language questions about candidate data
- Fast, vector-based semantic search using FAISS
- Clean, responsive UI

---

## 🏗️ Project Structure
recruiterAI-main/
├── BackEnd/ # Python backend (FastAPI, LangChain, FAISS)
├── FrontEnd/ # React frontend (chat interface)
├── README.md
├── package-lock.json
└── .gitignore


---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+

---

### Backend Setup (FastAPI)

``bash
cd recruiterAI-main/BackEnd
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload``

#### Backend will be available at: http://localhost:8000

### Frontend Setup (React)

``cd recruiterAI-main/FrontEnd
npm install
npm run start``

#### Frontend will be served at: http://localhost:3000

### Tech Stack
  
  - Backend: Python, FastAPI, LangChain, FAISS, OpenAI API

  - Frontend: React, JavaScript, Vite

  - Vector DB: FAISS (in-memory search)


### Installation Notes

  -  Backend uses OpenAI API and LangChain for NLP tasks

  -  FAISS index files are stored in BackEnd/vectorstore/

  -  Test data (e.g., resume.txt) should be present in the backend folder
