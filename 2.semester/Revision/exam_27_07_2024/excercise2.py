import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost", 9000))
while True:
    num = input ("CLIENT:")
    if num=="0":
        s.close()
    break # end the client
s.sendall(num.encode("utf-8"))
data = s.recv(1024).decode("utf-8")
print ("SERVER:", data )