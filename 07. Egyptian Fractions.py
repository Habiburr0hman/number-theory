def egyptian_fraction(p, q):
    num = 0
    n = 1
    arr = []
    err = 0.000001
    while abs(p/q - num) > err:
        if 1/n <= p/q - num:
            num += 1/n
            arr.append(n)
        n += 1
    return arr

frac = (5, 13)
arr = egyptian_fraction(frac[0], frac[1])
print(arr, sum([1/n for n in arr]), frac)