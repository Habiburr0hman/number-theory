def fibonacci(n):
    arr = [0, 1]
    while arr[-1] <= n:
        arr.append(arr[-1] + arr[-2])
    return arr[2:]

def zeckendorf(n):
    fibo = fibonacci(n)
    num = 0
    i = len(fibo) - 1
    arr = []
    while num < n and i >= 0:
        f = fibo[i]
        if n - num >= f:
            num += f
            arr.append(f)
            i -= 2
            continue
        i -= 1
    if num == n:
        return arr, num
    else:
        return None

# arr = zeckendorf(200)
# print(arr)

for i in range(1000):
    print(zeckendorf(i))