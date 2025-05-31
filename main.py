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
    "3602": "https://ministerial-rosalynd-brddxkj-321723bf.koyeb.app/",
    "3603": "https://vital-junie-ckejcjdjwj-419a3721.koyeb.app/",
    "saver": "https://protectorsop-2.onrender.com",
    "Txt": "https://txesc-4rql.onrender.com",
    "Txt2": "https://txesc-2.onrender.com",
    "Txt3": "https://txesc-1.onrender.com",
    "Txt4": "https://lulilele-3pci.onrender.com",
    "Txt5": "https://lulilele-1-1ryu.onrender.com",
    "Txt6": "https://upelckjwh.onrender.com",
    "Txt7": "https://protectorsop-1.onrender.com",
    "txt8": "https://txesc-mm88.onrender.com",
    "Server1": "https://serves.onrender.com",
    "PWEXTRACTOR": "https://protectorsop-4ulv.onrender.com",
    "SAMX1": "https://txesc-p3oa.onrender.com",
    "SAMX2": "https://txesc-79d0.onrender.com",
    "SAMX3": "https://txesc-vqbm.onrender.com",
    "SAMX4": "https://txesc-4jbw.onrender.com",
}

def send_requests():
    while True:
        for bot_name, url in SERVERS.items():
            try:
                response = requests.get(url)
                print(f"{bot_name} - Response: {response.status_code}, {response.text}")
            except Exception as e:
                print(f"{bot_name} - Error: {e}")
        
        time.sleep(90)  # Wait 60 seconds before sending the next batch

# Start the background thread
thread = threading.Thread(target=send_requests, daemon=True)
thread.start()

@app.route("/")
def home():
    return "Bot request sender is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
