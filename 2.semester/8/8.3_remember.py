import time

def remember(fn):
    execution1 = "ABC"
    def inner():
        nonlocal execution1
        if execution1 == "ABC":
            execution1 = fn()
        return execution1
    return inner()



@remember
def m1 ():
    return time.time()
print (m1())
print (m1())
time.sleep(2)
print (m1())
print (m1())