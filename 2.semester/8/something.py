def xx():
    a = 10

    try:
        print(a/0)
    except:
        print("Error ocurred")
    else:
        print("all good")
    finally:
        print("Now at the end")





def yy():
    a = 10
    print(a/0)


def yx():
    yy()

def bb():
    try:
        yx()
    except:
        print("Error caught in bb()")

xx()
bb()
try:
    yy()
except:
    "Error caught in regular try"
