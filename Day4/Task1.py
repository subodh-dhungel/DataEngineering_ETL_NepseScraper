def convertToInt(num, base):
    hexDigits = "0123456789ABCDEF"
    strNum = str(num)
    decimalValue = 0

    if(base == 8 or base == 2):
        for digit in strNum:
            decimalValue = decimalValue * base+ int(digit)
        return decimalValue
    elif(base == 16):
        hexNum = num.upper()
        for i, digit in enumerate(reversed(hexNum)):
            if digit in hexDigits:
                decimalValue += hexDigits.index(digit) * (16**i)
    
        return decimalValue

print(convertToInt("1a", 16))
print(convertToInt(58,8))
print(convertToInt(1101, 2))