# What is the sum of postive integer numbers
def sumOfDigits(n):
    # Step 3: condition (to manage unintentional cases) - the sum of postive integer numbers
    assert n >= 0 and int(n) == n, 'Write the postive integer numbers'
    # Step 2: Base case - stopping condition
    if n == 0:
        return 0
    else:
        # Step 1: Expected output
        return int(n%10) + sumOfDigits(int(n/10))
    
print(sumOfDigits(111111))