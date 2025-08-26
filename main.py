import time
import requests
import random
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from urllib.parse import parse_qs
from pymongo import MongoClient
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# MongoDB configuration
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv")
DB_NAME = "Cluster0"
COLLECTION_NAME = "servers"

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    logger.info("Connected to MongoDB")
except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {str(e)}")
    raise

# Fake user-agents
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
        for server in collection.find():
            ping_server(server['name'], server['url'])
        logger.info("=== Done. Sleeping 5 minutes ===")
        time.sleep(0.0001)  # 5 minutes

# HTTP server with form handling
class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Simple HTML form
        html = """
        <html>
        <body>
            <h1>Bot is Running!</h1>
            <h2>Add New Server</h2>
            <form method="POST" action="/add">
                <label>Name: </label><input type="text" name="name"><br><br>
                <label>URL: </label><input type="text" name="url"><br><br>
                <input type="submit" value="Add Server">
            </form>
            <h2>Remove Server</h2>
            <form method="POST" action="/remove">
                <label>Name: </label><input type="text" name="name"><br><br>
                <input type="submit" value="Remove Server">
            </form>
            <h3>Current Servers:</h3>
            <ul>
        """
        for server in collection.find():
            html += f"<li>{server['name']}: {server['url']}</li>"
        html += """
            </ul>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        params = parse_qs(post_data)

        if self.path == "/add":
            name = params.get('name', [''])[0].strip()
            url = params.get('url', [''])[0].strip()
            if name and url:
                # Check if name already exists
                if collection.find_one({"name": name}):
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(b"Server name already exists! <a href='/'>Go back</a>")
                else:
                    collection.insert_one({"name": name, "url": url})
                    logger.info(f"Added server: {name} - {url}")
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(b"Server added successfully! <a href='/'>Go back</a>")
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Missing name or URL! <a href='/'>Go back</a>")

        elif self.path == "/remove":
            name = params.get('name', [''])[0].strip()
            if collection.find_one({"name": name}):
                collection.delete_one({"name": name})
                logger.info(f"Removed server: {name}")
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Server removed successfully! <a href='/'>Go back</a>")
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Server not found! <a href='/'>Go back</a>")

def run_server():
    """Run a simple HTTP server."""
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, KeepAliveHandler)
    logger.info("Starting keep-alive HTTP server on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    try:
        run_pings()
    except KeyboardInterrupt:
        logger.info("Shutting down...")
        client.close()
