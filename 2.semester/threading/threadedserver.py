import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",8000))
s.listen()


def handle_client(address, client_socket):
    import random
    print("A client from address", address, "has just connected")
    words = ["running", "pinaple", "football", "arms"]
    word = words[random.randint(0, 3)]
    message_from_client = client_socket.recv(1024)

    print("Got the message from client : ", message_from_client.decode("utf-8"))
    message_from_client = message_from_client.decode("utf-8")
    if message_from_client == "bye":
        client_socket.close()
    #client_socket.sendall((b"recieved"))
    word_in_a_list = []
    for thing in word:
        word_in_a_list.append(thing)


    if message_from_client == word:
        client_socket.sendall((b"You have guessed the word"))
        client_socket.close()
    message_in_list = []
    for arg in message_from_client:
        message_in_list.append(arg)
    FoundStuff = "You have found "
    for arg in message_in_list:
        if arg in word_in_a_list:
            FoundStuff += f'{arg} at position {word_in_a_list.index(arg)} ,'
    if FoundStuff == "You have found ":
        client_socket.sendall((b"You have found nothing"))
    else:
        client_socket.sendall((FoundStuff.encode("utf-8")))
    message_from_client = client_socket.recv(1024)
while True:
    s.listen()
    client_socket, address = s.accept()
    t1 = threading.Thread(target=handle_client, args=(address, client_socket,))
    t1.start()


{{a,{a}},{a,{0}},0,{{a,b,c},{1,2}},{{{a,b,c},{1,2}}},2,a}


client_socket.close()

