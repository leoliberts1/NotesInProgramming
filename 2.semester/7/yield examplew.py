def x():
    return 5
    return 6

def y():
    yield 1
    yield 2
    yield 4
    yield 8


print(x())
i = y()
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))