from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os
from app.chatbot import get_chat_response

app = FastAPI(title="USDA Rural Development Chatbot")

# Load your API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def home():
    return {"message": "USDA Chatbot is running!"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    response = get_chat_response(message)
    return JSONResponse({"reply": response})
