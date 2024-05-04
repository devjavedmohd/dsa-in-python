'''
def factorial(n):
    # Ensure 'n' is a positive integer
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    k = 1  # Initialize the result variable
    
    # Loop from 1 to 'n' to calculate the factorial
    for i in range(1, n + 1):
        print(i)
        k *= i  # Multiply 'k' by 'i'
    
    return k

print(factorial(5))


# Test case for negative number (raises ValueError)
try:
    print(factorial(-1))
except ValueError as e:
    print(e)  # Output: "Factorial is not defined for negative numbers"
'''

def mean_median():
    numbers = []
    str_input = None
    sum_numbers = 0

    # Collect input until an empty string is entered

    while str_input != "":
        str_input = input("Enter a number (press Enter to finish): ")
        if str_input != "":
            numbers.append(float(str_input))
            sum_numbers += float(str_input)

    # numbers.sort()  # Sort the list of numbers

    # Calculate mean
    mean = sum_numbers / len(numbers)

    # Calculate median
    n = len(numbers)

    if n % 2 == 1:  # If the length of the list is odd
        median = numbers[n // 2]
    else:  # If the length of the list is even
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    return mean, median

mean, median = mean_median()

print("Mean:", mean)
print("Median:", median)
