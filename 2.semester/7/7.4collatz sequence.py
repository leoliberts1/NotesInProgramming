#if even - divide by two
#if odd - times 3 and -1
#up to 1

def collatz(number):
    results = []
    while number != 1:
        results.append(int(number))
        yield int(number)
        if number %2 != 0:
            number = number*3 +1
        else:
            number = number /2
    results.append(int(number))
    yield int(number)
    yield results
for x in collatz(127):
    print(x)