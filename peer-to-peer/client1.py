# client1.py
import socket
import stun

server = 'stun.l.google.com', 19302
client_port = 8000
client_addr = stun.get_ip_info()[0]

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((client_addr, client_port))

nat_type, _, host, port = stun.get_ip_info(s, server)
print(f'NAT Type: {nat_type}, Public IP: {host}, Public Port: {port}')

server_ip, server_port = input('Enter server IP address and port (e.g. 192.168.0.100:8001): ').split(':')
server_port = int(server_port)

s.sendto(f'hello from {client_addr}:{client_port}'.encode(), (server_ip, server_port))
data, remote_addr = s.recvfrom(1024)
print(f'Received from {remote_addr}: {data.decode()}')
s.close()
