letter_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
example = "threerznlrhtkjp23mtflmbrzq395three"

happyList = []

def WordsToNumbers(string):
    x = len(string)
    d = 0
    while (d + 2) < len(string):  # Corrected loop condition
        word = string[d:d + 3]  # Extract a substring of length 3
        if word in letter_numbers:
            happyList.append(word)
            d += 3  # Move to the next position
        elif len(string) - d > 3:  # Check if there's room for a 4-letter word
            word = string[d:d + 4]  # Extract a substring of length 4
            if word in letter_numbers:
                happyList.append(word)
                d += 4  # Move to the next position
            else:
                happyList.append(string[d])  # Append individual character
                d += 1  # Move to the next position
        else:
            happyList.append(string[d])  # Append individual character
            d += 1  # Move to the next position

    return happyList

print(WordsToNumbers(example))
