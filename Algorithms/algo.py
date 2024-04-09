# b)
### Convert the total times from seconds to days to confirm that we get 12.7 days for n = 40.

s = 0.000001  # time it takes for a single basic operation

# Fifth row of the table of total times, given in day,
#       with exponential growth rate = 2**n, for n = 10 .. 60
for n in range(10, 70, 10):
    text = f'For n = {n} and growth rate 2^n; Total time t is '
    if 2 ** n * s < 60:  # seconds here
        print(f"For n = {n} and growth rate 2^n; Total time t is {2 ** n * s} seconds")
    elif 2 ** n * s < 3600:  # minutes here
        print(f'{text}{2 ** n / 60 * s} minutes')
    elif 2 ** n * s < 3456000:  # hours here
        print(f'{text}{2 ** n / 3600 * s} hours')
    elif 2 ** n * s < 31536000:
        print(f'{text}{2 ** n / 3600 / 24 * s} days')
    elif 2 ** n * s < 3153600000:
        print(f'{text}{2 ** n / 3600 / 24 / 365 * s} years')
    elif 2 ** n * s >= 3153600000:
        print(f'{text}{2 ** n / 3600 / 24 / 365 / 100 * s} centuries')

    # print("For n =", n, "and growth rate 2^n; Total time t is", \
    #     round(((2**n)*s)/(60*60*24),3), "days")
# b)
### Convert the total times from seconds to days to confirm that we get 12.7 days for n = 40.
print("=============================")
s = 0.000000001  # time it takes for a single basic operation

# Fifth row of the table of total times, given in day,
#       with exponential growth rate = 2**n, for n = 10 .. 60
for n in range(10, 70, 10):
    text = f'For n = {n} and growth rate 2^n; Total time t is '
    if 2 ** n * s < 60:  # seconds here
        print(f"For n = {n} and growth rate 2^n; Total time t is {2 ** n * s} seconds")
    elif 2 ** n * s < 3600:  # minutes here
        print(f'{text}{2 ** n / 60 * s} minutes')
    elif 2 ** n * s < 3456000:  # hours here
        print(f'{text}{2 ** n / 3600 * s} hours')
    elif 2 ** n * s < 31536000:
        print(f'{text}{2 ** n / 3600 / 24 * s} days')
    elif 2 ** n * s < 3153600000:
        print(f'{text}{2 ** n / 3600 / 24 / 365 * s} years')
    elif 2 ** n * s >= 3153600000:
        print(f'{text}{2 ** n / 3600 / 24 / 365 / 100 * s} centuries')

    # print("For n =", n, "and growth rate 2^n; Total time t is", \
    #     round(((2**n)*s)/(60*60*24),3), "days")