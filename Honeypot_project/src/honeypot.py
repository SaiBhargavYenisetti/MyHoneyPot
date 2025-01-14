import socket
import json
from src.logger import log_connection
from src.response_handler import generate_response

def load_config():
    with open("src/config.json", "r") as f:
        return json.load(f)

def start_honeypot():
    config = load_config()
    host = config["host"]
    port = config["port"]
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Honeypot running on {host}:{port}")
        
        while True:
            conn, addr = server_socket.accept()
            log_connection(addr)
            response = generate_response()
            conn.sendall(response.encode())
            conn.close()

if __name__ == "__main__":
    start_honeypot()
