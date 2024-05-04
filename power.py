def power(base, exp):
    try:
        assert exp >= 0 and int(exp) == exp, 'Enter positive integer number'
        
        # base condition
        # any nubmer power 0 is 1
        # and 1 is self
        if exp == 0:
            return 1
        if exp == 1:
            return base
        return base * power(base, exp - 1)

    except AssertionError as error:
        print(error)

print(power(2,4))
print(power(2.2,4))
print(power(2,-1)) # Error will be occurd because its exponent is not a positive integer
print(power(2,3.2)) # Error will be occurd because its exponent is not a positive integer (it's an float number)








def power2(base, exp):
    try:
        assert exp >= 0 and int(exp) == exp, 'Enter positive integer number no float or other negative numbers'
        
        if exp == 0:
            return 1
        if exp == 1:
            return base
        # n * f(n, exp - 1)
        return base * power2(base, exp - 1)
    
    except AssertionError as error:
        print(error)
        
print(power2(3,4))