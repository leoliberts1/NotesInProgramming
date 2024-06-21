import socket

s = socket.socket()

host  = socket.gethostname()

port = 8080

s.bind((host,port))

s.listen(1)
print("Waiting for two connections")

conn,addr = s.accept()

print("client one has connected")

conn.send("welcome to the server".encode("UTF-8"))
print("waiting for 2nd connection")
conn1,addr1 = s.accept()
conn1.send("welcome to the server second client".encode("UTF-8"))
print("client 2 has connected")
while True:
    message = input(str(">>"))
    message = message.encode()

    conn.send(message)
    conn1.send(message)
    print("message sent")
    recv_message = conn.recv(1024).decode()
    recv1_message = conn1.recv(1024).decode()
    print("client", recv_message)
    print("client1", recv1_message)


