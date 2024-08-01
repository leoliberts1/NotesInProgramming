import threading
import socket
import csv

def handle_client(connection, client_address):
    print(f"Connected by {client_address}")
    person_in_question = connection.recv(1024).decode()
    person_looked_for = False
    #print(person_in_question)
    with open("passengers.csv", "r") as f:
        data = csv.DictReader(f)
        for person in data:
            #print(person)
            #print(person["PassangerId"],"This should be the id")

            if person["PassengerId"] == person_in_question:
                connection.send(person["Name"].encode("utf-8"))
                person_looked_for = True

    if not person_looked_for:
        connection.send("Passenger not found".encode("utf-8"))
    connection.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9000))
server.listen()
print("Server started and listening on port 9000")

while True:
    connection, client_address = server.accept()
    thread = threading.Thread(target=handle_client, args=(connection, client_address))
    thread.start()

