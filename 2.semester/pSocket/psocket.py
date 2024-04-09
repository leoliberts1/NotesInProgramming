import socket,requests
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(socket.gethostname() )# get name of the current host
print(socket.gethostbyname("www.google.at"))# get name of the current host
print(socket.gethostbyaddr("172.217.20.3")) # get host based on a given address
print(socket.getaddrinfo('www.python.org', 'http')) # additional info about a host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("example.com" , 80))
s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\nAccept: text/html\r\n\r\n")
print(str(s.recv(4096), 'utf-8'))
s.close()

x = requests.get("http://example.com")
print (x.text)
# Connecting to a local server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9000))
msg = b"Hi Server" # can also use .encode('utf-8')
s.send(msg)
message_from_server = s.recv(4096)
s.close()