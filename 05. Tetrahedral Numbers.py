def tetrahedral_number(n):
    arr = []
    num = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            num += j
        arr.append(num)
    return arr, num

def tetrahedral_closed(n):
    arr = []
    for i in range(1, n+1):
        num = (i**3 + 3*(i**2) + 2*i) // 6
        arr.append(num)
    return arr, num

# arr, num = tetrahedral_number(10000)
# print(arr, num)

arr, num = tetrahedral_closed(10000)
print(arr, num)