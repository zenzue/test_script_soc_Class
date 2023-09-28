import socket

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
    
        print(f"Server is Listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address} has been established.")

            with client_socket:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    client_socket.sendall(data)

if __name__ == "__main__":
    server_host = "192.168.100.5"
    server_port = 1337
    start_server(server_host, server_port)