import time
import requests
import random

# List of servers in {Name: URL} format
SERVERS = {
    "Server": " https://serves-rvvg.onrender.com",
    "Jaggo": "https://jaggo.onrender.com/",
    "SAMX 3": "https://txesc-vqbm-vnkh.onrender.com",
    "7th": "https://txesc-o52c.onrender.com",
    "Tryterbit": "https://txesc-phy7.onrender.com",
    "Savers": "https://txesc-iesl.onrender.com",
    "SAMX 2": "https://txesc-80ix.onrender.com",
    "4th": "https://txesc-aopv.onrender.com",
    "2nd": "https://txesc-1-r75p.onrender.com",
    "3rd": "https://txesc-1-s62m.onrender.com",
    "10th": "https://txesc-1-gq8v.onrender.com",
    "9th": "https://txesc-1-bkiz.onrender.com",
}

# Fake user-agents like UptimeRobot/browsers
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.65 Mobile Safari/537.36",
    "UptimeRobot/2.0 (http://uptimerobot.com/)",
]

def ping_server(name, url):
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"[+] {name} ({url}) - Status: {response.status_code}")
    except Exception as e:
        print(f"[-] {name} ({url}) - Failed: {e}")

if __name__ == "__main__":
    while True:
        print("\n=== Pinging Servers ===")
        for name, url in SERVERS.items():
            ping_server(name, url)
        print("=== Done. Sleeping 5 minutes ===\n")
        time.sleep(0.1)  # 5 minutes
