def decimal_to_ternary(dec):
    ter = ""
    while dec > 0:
        ter = str(dec % 3) + ter
        dec //= 3
        
    return ter

def balanced_ternary(n):
    num = n
    bal_ter = ""
    arr = []
    while n > 0:
        rem = n % 3
        n //= 3

        if rem == 2:
            rem = -1
            n += 1
        
        if rem == 0:
            bal_ter = "0" + bal_ter
            arr.append(0)
        elif rem == 1:
            bal_ter = "1" + bal_ter
            arr.append(1)
        else:
            bal_ter = "Z" + bal_ter
            arr.append(-1)

    string_arr = []
    for i in range(len(arr)):
        string_arr.append("{}.3^{}".format(str(arr[i]), i))
    
    string = " + ".join(reversed(string_arr))
    print("{} = {}".format(num, string))

    return bal_ter

bal_ter = balanced_ternary(238)
print(bal_ter)