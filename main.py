from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

SERVERS = {
    "Server": " https://serves-rvvg.onrender.com ",
    "Jaggo": "https://jaggo.onrender.com/",
    "SAMX 3": "https://txesc-vqbm-vnkh.onrender.com",
    "7th": "https://txesc-o52c.onrender.com",
    "Tryterbit": "https://txesc-phy7.onrender.com",
    "Savers": "https://txesc-iesl.onrender.com",
    "SAMX 2": "https://txesc-80ix.onrender.com",
    "4th": "https://txesc-aopv.onrender.com",
    "2nd": "https://txesc-8ejn.onrender.com",
    "3rd": "https://txesc-1-s62m.onrender.com",
    "10th": "https://txesc-1-gq8v.onrender.com",
    "Server": " https://serves-rvvg.onrender.com ",    
    "Jaggo": "https://jaggo.onrender.com/",
    "SAMX 3": "https://txesc-vqbm-vnkh.onrender.com",
    "7th": "https://txesc-o52c.onrender.com",
    "Tryterbit": "https://txesc-phy7.onrender.com",
    "Savers": "https://txesc-iesl.onrender.com",
    "SAMX 2": "https://txesc-80ix.onrender.com",
    "4th": "https://txesc-aopv.onrender.com",
    "2nd": "https://txesc-8ejn.onrender.com",
    "3rd": "https://txesc-1-s62m.onrender.com",
    "10th": "https://txesc-1-gq8v.onrender.com",
    "Server": " https://serves-rvvg.onrender.com ",    
    "Jaggo": "https://jaggo.onrender.com/",
    "SAMX 3": "https://txesc-vqbm-vnkh.onrender.com",
    "7th": "https://txesc-o52c.onrender.com",
    "Tryterbit": "https://txesc-phy7.onrender.com",
    "Savers": "https://txesc-iesl.onrender.com",
    "SAMX 2": "https://txesc-80ix.onrender.com",
    "4th": "https://txesc-aopv.onrender.com",
    "2nd": "https://txesc-8ejn.onrender.com",
    "3rd": "https://txesc-1-s62m.onrender.com",
    "10th": "https://txesc-1-gq8v.onrender.com",
}

def send_requests():
    while True:
        for bot_name, url in SERVERS.items():
            try:
                response = requests.get(url)
                print(f"{bot_name} - Response: {response.status_code}")
            except Exception as e:
                print(f"{bot_name} - Error: {e}")
        
        time.sleep(0.001)  # Wait 60 seconds before sending the next batch

# Start the background thread
thread = threading.Thread(target=send_requests, daemon=True)
thread.start()

@app.route("/")
def home():
    return "Bot request sender is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
