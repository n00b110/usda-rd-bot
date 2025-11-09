from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def home():
    return {"message": "USDA Chatbot is running!"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    # For now, we’ll just call the OpenAI API directly
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful USDA Rural Development assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    return JSONResponse({"reply": response["choices"][0]["message"]["content"]})
