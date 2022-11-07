
from dotenv import load_dotenv
from flask import Flask, request

# Twilio
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from flask_ngrok import run_with_ngrok
from playsound import playsound

# bot
from textToSpeech import synthesizeText
from whatsappBot import sendWspMessage

#loads .env variables
load_dotenv()

# Create Twilio client
account_sid = 'ACfb5da8c1fbd6c6cb63e4b7b440e00719' 
api_key = '275e181f34867d7661c684ff0cd66ca4'
twilio_client = Client(account_sid, api_key)

saved_messages = []

# Create Flask app web server
app = Flask(__name__) #app name
run_with_ngrok(app)

def save(message):
    saved_messages.append(message)
    print(saved_messages)
    return message

def hear_messages():
    for message in saved_messages:
        synthesizeText(message)
        playsound("output.mp3")
    return "mensaje escuchado"

def delete_messages():
    saved_messages.clear()
    print(saved_messages)
    return "mensajes guardados"

@app.route("/message", methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
    return save(message)

@app.route("/hearmsgs", methods=['POST'])
def hear():
    hear_messages()
        
@app.route("/repeatmsgs", methods=['POST'])
def repeat():
    hear_messages()


@app.route("/deletemsgs", methods=['POST'])
def delete():
    delete_messages()

@app.route('/')
def hello_world():
    return 'Hello Pepe!'
       
if __name__ == "__main__":	
    app.run()
    
