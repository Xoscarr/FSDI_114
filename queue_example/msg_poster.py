import request 
from datetime import datetime
from random import choice

MESSAGE = {
    "message":"",
    "timestamp":""
}

def post_message(content):
    msg = MESSAGE
    msg["message"] = content
    msg["timestamp"] = datetime.now()strftime("%F %H:%M:%S")
    request.post("http://127.0.0.1:5000/messages", json=msg)

if __name__ == "__main__":
    greetings = ["hello", "hey", "howdy", "what's up", "hola"]
    for _ in range(100):
        selected_greetings = choice(greetings)
        post_message(selected_greeting)