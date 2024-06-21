import time
import threading

class MyCounter(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        count = 0
        while count <= 1000:
            print(self.name + str(count))
            count +=1
            time.sleep(1)
C_counter = MyCounter("C")
C_counter.start()

D_counter = MyCounter("D")
D_counter.start()

print("Main branch is done")