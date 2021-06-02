def binaryAddition(a, b):
    result = ""
    carry = 0

    while a or b or carry:
        # sum the digits
        sum = int(a[-1]) + int(b[-1]) + carry

        if sum > 1:
            result = str(sum % 2) + result
            carry = 1

        else:
            result = str(sum) + result
            carry = 0

        a = a[0:-1]
        b = b[0:-1]

    return result


a = "000010100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"

print(binaryAddition(a, b))
