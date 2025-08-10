def decimal_to_binary(n):
    if n == 0:
        return "0"
    else:
        bin = ""
        while n != 0:
            if n % 2 == 0:
                bin = "0" + bin
            else:
                bin = "1" + bin
            n //= 2
        return bin

def binary_recursive(n):
    if n > 0:
        binary_recursive(n // 2)
        print(n % 2, end="")

def binary_to_decimal(bin):
    num = 0
    for i in range(len(bin)):
        num += int(bin[len(bin) - i - 1]) * (2**i)
    return num


bin = decimal_to_binary(10)
print(bin)

# binary_recursive(10)

dec = binary_to_decimal(bin)
print(bin, dec)