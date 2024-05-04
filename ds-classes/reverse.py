def reverse(array):
    for i in range(0, int(len(array)/2)):
        other = len(array) - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)


reverse([1, 2, 3, 4, 5, 7, 8, 6, 10, 9])
