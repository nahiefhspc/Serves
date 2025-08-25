import time
import requests
import random
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Configure logging for better debugging on Render
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# List of servers in {Name: URL} format
SERVERS = {
    "Server": " https://serves-rvvg.onrender.com",
    "Jaggo": "https://jaggo.onrender.com/",
    "SAMX 3": "https://txesc-1-v8xj.onrender.com",
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
    """Ping a server and log the result."""
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        logger.info(f"{name} ({url}) - Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"{name} ({url}) - Failed: {str(e)}")

def run_pings():
    """Run the ping loop indefinitely."""
    while True:
        logger.info("=== Pinging Servers ===")
        for name, url in SERVERS.items():
            ping_server(name, url)
        logger.info("=== Done. Sleeping 5 minutes ===")
        time.sleep(0.0001)  # 5 minutes

# HTTP server to keep Render happy (prevents idling)
class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Service is running!")

def run_server():
    """Run a simple HTTP server to respond to Render's health checks."""
    server_address = ('', 8000)  # Render expects a web server on the assigned port
    httpd = HTTPServer(server_address, KeepAliveHandler)
    logger.info("Starting keep-alive HTTP server on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    # Run the HTTP server in a separate thread to keep Render from idling
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Run the ping loop in the main thread
    try:
        run_pings()
    except KeyboardInterrupt:
        logger.info("Shutting down...")
