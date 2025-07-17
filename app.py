import os
from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["GET", "POST"])
def voice():
    # simple debug print so we know the route fires
    print(f"DEBUG: /voice hit via {request.method}", flush=True)
    resp = VoiceResponse()
    resp.say("Hello from your AI Secretary scaffold. We'll add language selection next.")
    resp.hangup()
    return Response(str(resp), mimetype="text/xml")

if __name__ == "__main__":
    # Use 5001 to avoid conflict with macOS AirPlay on 5000
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
