def division_algorithm(a, b):
    # a = bq + r, 0 <= r < b
    q = a // b
    r = a - b*q
    print("{} = {} . {} + {}".format(a, b, q, r))

division_algorithm(100, 7)