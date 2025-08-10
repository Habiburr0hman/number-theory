def pentagonal_number(n):
    arr = []
    num = 0
    for i in range(1, n+1):
        num += 3*i - 2
        arr.append(num)
    return arr, num 

def pentagonal_closed(n):
    arr = []
    for i in range(1, n+1):
        num = (3*(i**2) - i) // 2
        arr.append(num)
    return arr, num

arr, num = pentagonal_number(100000)
print(arr, num)