def binary_to_hexadecimal(bin):
    hex_digits = "0123456789ABCDEF"
    hex = ""
    remainder = len(bin) % 4
    if remainder != 0:
        bin = "0" * (4 - remainder) + bin

    for i in range(0, len(bin), 4):
        digit_block = bin[i:i+4]
        dec = 0
        for j in range(4):
            dec += int(digit_block[j]) * (2**(3-j))
        hex += hex_digits[dec]
        
    return hex

def hexadecimal_to_binary(hex):
    mapping_dict = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", 
                    "4": "0100", "5": "0101", "6": "0110", "7": "0111", 
                    "8": "1000", "9": "1001", "A": "1010", "B": "1011", 
                    "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    bin = ""
    for i in hex:
        bin += mapping_dict[i] 

    bin = bin.lstrip("0")
    return bin

hex = binary_to_hexadecimal("111001010")
print(hex)
bin = hexadecimal_to_binary(hex)
print(bin)