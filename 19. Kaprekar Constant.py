def operate(n):
    string = str(n)
    ascended = int("".join(sorted(string)))
    descended = int("".join(reversed(sorted(string))))
    return descended - ascended

for n in range(1000, 10000):
    if operate(n) == n:
        print("n = {} memenuhi T(n) = n".format(n))

for n in range(1000, 10000):
    num = n
    arr = [n]
    k = 0
    while operate(n) >= 1000 and n != 6174:
        n = operate(n)
        arr.append(n)
        k += 1
    if k == 0:
        print("{} tidak dapat dioperasikan.".format(num))
    else:
        print("{} | {} | {} langkah".format(num, arr, k))