# whatsappbot_using-Twilio-s-API
# WhatsAppBot - AI Powered Chatbot using Flask and Twilio

WhatsAppBot is a conversational chatbot powered by OpenAI's GPT-3.5-turbo, designed to respond to messages sent via WhatsApp using Twilio's API. This project allows users to engage in intelligent conversations through a simple messaging interface.

## Features
- Real-time conversation using OpenAI GPT-3.5-turbo
- WhatsApp integration via Twilio API
- Maintains conversation history for better context
- Flask backend with CORS support for enhanced flexibility

## Prerequisites
Ensure you have the following installed:
- Python 3.10+
- `openai` library
- `Flask`
- `Flask-CORS`
- `python-dotenv`
- `twilio`

## Installation
1. **Clone the Repository**
```bash
git clone https://github.com/thilageeswariguruviah/whatsappbot.git
cd whatsappbot
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Set Up Environment Variables**
Create a `.env` file in the root directory and add the following keys:
```
OPENAI_API_KEY=your_openai_api_key_here
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
twilio_api_secret = your twilio_api_secret
twilio_api_key = your twilio_api_key
```

4. **Configure Twilio Webhook**
- Go to your Twilio dashboard.
- Set the **Webhook URL** for incoming messages to:
```
http://<your-server-url>/whatsapp
```

## Running the Application

1. **Start the Flask Application**
```bash
python app.py
```

2. **Test with Twilio Sandbox for WhatsApp**
- Connect your phone number with Twilio Sandbox for WhatsApp.
- Send a message to your Twilio WhatsApp number to test the bot's response.

## Project Structure
```
.
├── app.py             # Flask API for WhatsApp Webhook
├── llm.py             # Logic to interact with OpenAI's GPT-3.5-turbo
├── .env               # Environment variables (add your API key here)
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

## Requirements File (`requirements.txt`)
```
openai
flask
flask-cors
twilio
python-dotenv
```

## Known Issues
- If the bot fails to generate a response, check if your OpenAI API key is correctly set in the `.env` file.
- Ensure your Twilio webhook URL matches the endpoint in `app.py`.
- Verify that both `app.py` and Twilio settings are correctly configured.

## Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue for improvements.


