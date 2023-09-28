import psutil

def list_network_connections():
    connections = psutil.net_connections(kind='inet')
    print("Local Address\t\tLocal Port\tRemote Address\tRemote Port\tStatus")

    for connection in connections:
        laddr = f"{connection.laddr.ip}:{connection.laddr.port}"
        raddr = f"{connection.raddr.ip}:{connection.raddr.port}" if connection.raddr else ""
        status = connection.status
        print(f"{laddr}\t{raddr}\t{status}")

if __name__ == "__main__":
    print("Listening incoming and outgoing connections")
    list_network_connections()
        