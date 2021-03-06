from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if 'hello there' in body:
        resp.message("Hello, it is a pleasure to meet you!")
    elif body == 'bye':
        resp.message("Goodbye for now- check in with me later!")
    else:
        resp.message(f"{body} <-- this is what you sent\n \
        {type(body)} <-- body type")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
