def perfect_square(n):
    arr = []
    for i in range(1, n+1):
        num = i**2
        arr.append(num)
    return arr, num

arr, num = perfect_square(10)
print(arr, num)