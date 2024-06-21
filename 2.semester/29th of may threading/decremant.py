import threading
x = 0

def increment():
    global x
    for i in range(1000000):
        x = x+1
def decrement():
    global x
    for i in range(1000000):
        x = x-1
t1 = threading.Thread(target=increment)
t1.start()
print("t1 started")
t2 = threading.Thread(target=decrement)
t2.start()
print("t2 started")
print(x)