import openai
import os
import json

# This is a temporary simple version
# Later you can upgrade it with embeddings or vector search

def get_chat_response(user_message):
    # Simple USDA context — later replace with real data loading
    context = """
    USDA Rural Development programs provide loans and grants for housing, business, and community development in rural areas.
    Example programs include:
    - Single Family Housing Guaranteed Loan Program
    - Rural Business Development Grants
    - Community Facilities Direct Loan & Grant Program
    """

    system_prompt = f"You are a helpful USDA assistant. Use this context to answer accurately.\n{context}"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.3
    )

    return response["choices"][0]["message"]["content"]
