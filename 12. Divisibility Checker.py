def divisibility_check(m, n):
    if m % n == 0:
        print("{} is divisible by {}".format(m, n))
    else:
        print("{} is not divisible by {}".format(m, n))

divisibility_check(10, 2)