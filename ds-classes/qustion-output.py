'''
x = 64
# for i in range(2, 6):
i = 2
while i < 6:
    x //= 2
    print(i*i, x)
    i += 1
''' 
def q5():
    z = 0
    for i in range(1, 10):
        if (i + 1 // 2) % 7 == 0:
            break
        else:
            z += int(i % 2 == 0)
            print(z)
    else:
        print('end')
q5()