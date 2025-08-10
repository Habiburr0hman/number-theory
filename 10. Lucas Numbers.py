def lucas_number(n):
    a_1 = 1
    a_2 = 3
    arr = [a_1, a_2]
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])
    return arr, arr[n-1]

arr, num = lucas_number(10)
print(arr, num) 