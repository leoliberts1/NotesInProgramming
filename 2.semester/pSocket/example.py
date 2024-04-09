import socket
# Connecting to a local server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("example.com" , 80))
s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\nAccept: text/html\r\n\r\n")
print(str(s.recv(4096), 'utf-8'))
s.close()
import requests
x = requests.get("http://example.com")
print (x.text)