from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

SERVERS = {
    "BOT 1": "https://bot1server.koyeb.app/",
    "BOT 2": "https://bot2server.koyeb.app/",
    "SERVER": "https://prime-robby-bedicjjwsh-132a0edd.koyeb.app/",
    "MOTION": "https://mute-mommy-brcjjejdj-0be63631.koyeb.app/",
    "Leech1": "https://concerned-ellyn-goejdj-c75adff2.koyeb.app/",
    "Leech2": "https://absent-magdalen-ywdjcjs-ba359b35.koyeb.app/",
    "Leech3": "https://pregnant-thrush-qfkcsjjc-ebbb9db4.koyeb.app/",
    "Leech4": "https://current-sherilyn-wsdksk-454c250b.koyeb.app/",
    "Signup": "https://steady-darelle-qxckehc-2bf9bb53.koyeb.app/",
    "DreamMit": "https://prominent-julianna-brxwsx-867f3a56.koyeb.app/",
    "2ndaccount": "https://molecular-sondra-qcvosch-b97baa7f.koyeb.app/",
}

def send_requests():
    while True:
        for bot_name, url in SERVERS.items():
            try:
                response = requests.get(url)
                print(f"{bot_name} - Response: {response.status_code}, {response.text}")
            except Exception as e:
                print(f"{bot_name} - Error: {e}")
        
        time.sleep(100)  # Wait 60 seconds before sending the next batch

# Start the background thread
thread = threading.Thread(target=send_requests, daemon=True)
thread.start()

@app.route("/")
def home():
    return "Bot request sender is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
