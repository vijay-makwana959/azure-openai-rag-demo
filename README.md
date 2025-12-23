# Azure OpenAI RAG Demo

This project demonstrates a simple **RAG-based AI chatbot** using **Azure OpenAI** with
CI/CD using **GitHub Actions** and **Jenkins Multibranch Pipeline**.

## Architecture
- FastAPI backend
- Streamlit UI
- Azure OpenAI (GPT)
- Dockerized application

## Run Locally

### Backend
```bash
uvicorn app.main:app --reload
