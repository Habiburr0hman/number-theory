def modified_division_algorithm(a, b):
    # a = bq + r, -b/2 <= r < b/2
    q = a // b
    r = a - b*q
    if r > b/2:
        q += 1
        r -= b
        print("{} = {} . {} + ({})".format(a, b, q, r))
    else:
        print("{} = {} . {} + {}".format(a, b, q, r))
  
modified_division_algorithm(102, 7)