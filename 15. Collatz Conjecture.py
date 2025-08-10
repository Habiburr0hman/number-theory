def collatz_conjecture(n):
    arr = [n]
    step = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (3*n + 1) // 2
        arr.append(n)
        step += 1
    return arr, step

arr, step = collatz_conjecture(10)
print(arr, step)

# for i in range(1, 10000):
#     arr, step = collatz_conjecture(i)
#     print(arr, step)