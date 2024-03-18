
def count_pandigital_numbers(n):
    def is_pandigital(num_str):
        return all(str(i) in num_str for i in range(0, 10))
    from itertools import permutations
    count = 0
    for perm in permutations(range(10)):
        num_str = ''.join(map(str, perm))
        if is_pandigital(num_str):
            count += int(num_str)
    return count

n = 1  # Adjust this to the desired number of digits
result = count_pandigital_numbers(n)
print(f"Number of {n}-digit pandigital numbers: {result}")


