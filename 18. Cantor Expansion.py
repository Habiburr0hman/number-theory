def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def cantor_expansion(n):
    num = n
    count_dict = {}
    while n > 0:
        m = 1
        while factorial(m) <= n:
            m += 1
        
        f = factorial(m-1)
        k = 0
        while f <= n:
            n -= f
            k += 1
        count_dict[m-1] = k

    arr = []
    for key, value in count_dict.items():
        arr.append("{}.{}!".format(value, key))
    string = " + ".join(arr)

    print("{} = {}".format(num, string))
    return count_dict

for i in range(1, 101):
    cantor_expansion(i)
    