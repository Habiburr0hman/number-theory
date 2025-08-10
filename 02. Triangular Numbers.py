def triangular_number(n):
    arr = []
    num = 0
    for i in range(1, n+1):
        num += i
        arr.append(num)
    return arr, num

def triangular_closed(n):
    arr = []
    for i in range(1, n+1):
        num = i*(i+1) // 2
        arr.append(num)
    return arr, num

arr, num = triangular_number(100000)
print(arr, num)