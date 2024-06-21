import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

    welcome_msg = client.recv(1024).decode()
    print(welcome_msg, end="")
    name = input()
    client.send(name.encode())

    num_questions_msg = client.recv(1024).decode()
    print(num_questions_msg, end="")
    num_questions = input()
    client.send(num_questions.encode())

    for _ in range(int(num_questions)):
        question_msg = client.recv(1024).decode()
        print(question_msg, end="")
        answer = input()
        client.send(answer.encode())
        feedback_msg = client.recv(1024).decode()
        print(feedback_msg)

    final_msg = client.recv(1024).decode()
    print(final_msg)

    client.close()

if __name__ == "__main__":
    main()
