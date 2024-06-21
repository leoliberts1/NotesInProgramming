
def decorate_this(fn):
    print("this is magic")
    def inner_function():
        print("before")
        fn()
        print("afterwards")
    return inner_function()

@decorate_this
def hello():
    print("this is helloooo :)")











