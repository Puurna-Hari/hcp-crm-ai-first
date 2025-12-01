# AI-First CRM – HCP Interaction Logging (FastAPI + LangGraph + React)

This repository contains both the backend and frontend implementation for an  
AI-first **Healthcare Professional (HCP) CRM Interaction Logging System** built as part of the  
Round-1 Assignment.

The goal is to build a CRM module where field reps can log interactions using:
- A structured form  
- A conversational chat interface  
- An AI agent powered by **LangGraph + Groq LLM (gemma2-9b-it)**  

---

# 🚀 Project Overview

## 🔹 Frontend
- React (Vite)
- Redux Toolkit
- Tailwind CSS
- Google Inter font

Modern UI for:
- Selecting HCPs  
- Logging interactions  
- Chat-based interaction logging  
- Viewing AI summaries  
- Viewing interaction history  

---

## 🔹 Backend
- FastAPI
- SQLAlchemy + PostgreSQL / MySQL
- LangGraph AI Agent
- Groq LLM (gemma2-9b-it)
- Modular CRUD architecture

---

## 🔹 AI Agent (LangGraph)
Implements **5 key tools**:

1. Log Interaction (mandatory)  
2. Edit Interaction (mandatory)  
3. Get HCP Details  
4. Get Past Interactions  
5. Next Best Action Recommendation (NBA)  

---

# 🧠 Architecture Diagram (High-level)

```
React UI  → Redux → Axios → FastAPI Backend → LangGraph Agent → Groq LLM
       ↑                                                ↓
       └────────────── Interaction Response (AI Summary)
```

---

# ⚙️ How to Run the Backend
```bash
cd backend
uvicorn backend.app.main:app --reload
```

Backend URL: http://127.0.0.1:8000  
API Docs: http://127.0.0.1:8000/docs

---

# 💻 How to Run the Frontend
```bash
cd frontend
npm install
npm run dev
```

Frontend URL: http://localhost:3000

---

# 📦 Folder Structure
```
frontend/   → React + Redux + Tailwind UI  
backend/    → FastAPI + LangGraph agent  
README.md   → This file
```

---

# 👤 Author
**Puurna Hari**  
GitHub: https://github.com/Puurna-Hari
