# Client.py
# Simple chat system, client based on udp
# Ib Helmer Nielsen, UCN october 2023
import socket

# Opret en UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Angiv serverens adresse og port
server_address = ('server_ip', 12345)  # Erstat 'server_ip' med serverens IP-adresse

while True:
    message = input("Skriv en besked: ").encode()
    client_socket.sendto(message, server_address)

    data, _ = client_socket.recvfrom(1024)
    print(f"Modtaget svar fra serveren: {data.decode()}")
