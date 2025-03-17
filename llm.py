# llm.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-3.5-turbo"  # or "gpt-4" if you have access

def generate_response(user_input, conversation_history=None):
    if conversation_history is None:
        conversation_history = []
    
    # Append the incoming user message for context.
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=0.7,
            max_tokens=150
        )
        reply = response.choices[0].message["content"].strip()
        # Append the AI's reply to maintain conversation history.
        conversation_history.append({"role": "assistant", "content": reply})
        return reply, conversation_history
    except Exception as e:
        print("Error generating response:", e)
        return "Sorry, I encountered an error processing your request.", conversation_history
