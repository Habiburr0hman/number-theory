def erdos_straus_conjecture(p):
    arr = []
    err = 0.000001
    for i in range(2, p+1):
        n = 1
        num = 0
        sub_arr = [i, []]
        while abs(4/i - num) > err:
            if 1/n < 4/i - num:
                num += 1/n
                sub_arr[1].append(n)
            n += 1
        arr.append(sub_arr)
    return arr

arr = erdos_straus_conjecture(100)
print(arr)