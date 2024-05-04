def firstMethod():
    secondMethod()
    print('It is first Method')
    
def secondMethod():
    thirdMethod()
    print('It is second Method')

def thirdMethod():
    fourthMethod()
    print('It is third Method')

def fourthMethod():
    print('It is fourth Method')

# firstMethod()
def recursiveMethod(n):
    # print(n)
    if n < 1:
        print('n is less than 1')
    else:
        recursiveMethod(n - 1)
        print(n)

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be postive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n - 1)

def fibonnaci(n):
    assert n >= 0 and int(n) == n, 'The fibonnacci number cannot be negative integer number'
    if n in [0,1]:
        return n
    else:
        print('index', n)
        return fibonnaci(n-1) + fibonnaci(n -2) 

def main():
    # firstMethod()
    # recursiveMethod(5)
    # print(factorial(4))
    print(fibonnaci(4))

if __name__ == '__main__':
    main()