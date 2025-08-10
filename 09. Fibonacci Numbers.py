def fibonacci(n):
    a_0 = 0
    a_1 = 1
    arr = [a_0, a_1]
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr, arr[n]

arr, num = fibonacci(5)
print(arr, num)