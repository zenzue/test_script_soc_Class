import socket

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connection to {host}:{port} has been established.")

        while True:
            message = input("Enter message (type 'exit' to quit): ")
            if message.lower() == "exit":
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received from server ", data.decode())

if __name__ == "__main__":
    server_host = "192.168.100.5"
    server_port = 1337
    start_client(server_host, server_port)