#Prompting the user to input a number to check if it's happy
n = input("Enter number to see if its happy: ")

#Defining a function 'happy' that takes an integer as input
def happy(n):
  # Converting the number to a list of digits
  s = list(str(n))
  # Initializing a variable to store the sum of squares of digits
  sum = 0
  # Looping through each digit in the number
  for i in s:
      # Adding the square of each digit to the sum
      sum += int(i)**2
  # Checking if the sum equals 1
  if sum == 1:
    # If sum is 1, return True (number is happy)
    return True
  else:
    # If sum is not 1, recursively call the 'happy' function with the sum
    return happy(sum)

#Printing the result of the 'happy' function with the input number
print(happy(n))