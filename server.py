import os
import socket
import threading

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 5000)) 

FLAG = os.getenv("FLAG", "FLAG{default_flag}") 
CORRECT_PASSWORD = os.getenv("PASSWORD", "defualt") 
OBFUSCATED_PASSWORD = "ba 60 a7 ee 1c 73 90 cf 47 9a 17"

def handle_client(conn, addr):
    """Handles a single client connection."""
    try:
        conn.sendall(b"Welcome to the Reverse Engineering Challenge!\n")
        conn.sendall(f"The obfuscated password is: {OBFUSCATED_PASSWORD}\n".encode())
        conn.sendall(b"Enter the correct password: ")

        user_input = conn.recv(1024).decode().strip()

        if not user_input:
            conn.sendall(b"No input received. Connection closing.\n")
        elif user_input == CORRECT_PASSWORD:
            conn.sendall(f"Correct! Here is your flag: {FLAG}\n".encode())
        else:
            conn.sendall(b"Incorrect password! Try again.\n")
    
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()

def start_server():
    """Starts the CTF server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(5)

        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            print(f"Connection from {addr}")
            
            # Handle client in a separate thread
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()
