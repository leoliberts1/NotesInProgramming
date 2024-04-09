import threading

def printingnum(code):
    for i in range(1000):
        print(code,i)

t1 = threading.Thread(target=printingnum, args=("Apple",))
t2 = threading.Thread(target=printingnum, args=("Banana",))
t3 = threading.Thread(target=printingnum, args=("ice cream",))
t4 = threading.Thread(target=printingnum, args=("Boat",))
t5 = threading.Thread(target=printingnum, args=("Pinaple",))
t6 = threading.Thread(target=printingnum, args=("Orange",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()