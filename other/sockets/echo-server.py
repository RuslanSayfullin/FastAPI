import socket

HOST = "127.0.0.1"  # Standart loopback interface address (localhost)
PORT = 65432        # Port to listen on (non privileged ports are > 1023)

def server(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

if __name__ == "__main__":
    server(HOST, PORT)    