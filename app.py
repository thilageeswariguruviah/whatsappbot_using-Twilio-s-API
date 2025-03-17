# app.py
from flask import Flask, request, Response
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse
import logging
from dotenv import load_dotenv
from llm import generate_response
import os

load_dotenv()
app = Flask(__name__)
CORS(app)  # Enable CORS if needed
logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    # Extract incoming message and sender info from Twilio's POST request
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")
    app.logger.info(f"Received message from {sender}: {incoming_msg}")

    # Process the incoming message through your LLM to generate a response.
    # You can maintain conversation history if desired.
    reply, _ = generate_response(incoming_msg)
    
    # Build the response using Twilio's MessagingResponse
    resp = MessagingResponse()
    resp.message(reply)
    app.logger.info(f"Sent reply: {reply}")
    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
