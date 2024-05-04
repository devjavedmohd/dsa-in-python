
# f(n) = n%2 + 10 * f(n/2) --  formula of converting binary to decimal using recursive method
def binaryToDecimal(n):
    try:
        assert int(n) == n, 'Enter valid integer number'
        if n == 0:
            return 0
        else:
            return n % 2 + 10 * binaryToDecimal(int(n / 2))
    except AssertionError as error:
        print(error)

print(binaryToDecimal(1))