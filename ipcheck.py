import socket

hostname = input('domain name: ')
ip_address = socket.gethostbyname(hostname)

print(f'Domain Name: {hostname}')
print(f'IP Address: {ip_address}')

