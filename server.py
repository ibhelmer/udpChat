# Server.py
# Simple chat server, based on UDP protocol
# Ib Helmer Nielsen, UCN october 2023
import socket

# Opret en UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Angiv serverens adresse og port
server_address = ('0.0.0.0', 12345)

# Bind socket til serveradressen
server_socket.bind(server_address)

print("Serveren kører...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Modtaget besked fra {client_address}: {data.decode()}")

    reply_message = input("Svar: ").encode()
    server_socket.sendto(reply_message, client_address)
