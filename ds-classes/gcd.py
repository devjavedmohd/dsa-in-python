# Greater Common divisor (GCD)

def gcd(a, b):
    try:
        assert b >= 0 and int(b) == b, 'Not a valid entry for Greater Common divisor'
        if a < 0:
            a = -1 * a
        if b < 0: 
            b = -1 * b
        if b == 0:
            return a
        else: 
            return gcd(b, a % b)
    except AssertionError as error:
            print(error)

print(gcd(48, 18))