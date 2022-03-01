import turtle
def decimaltohex(decimal_value):
    hex = ' '

    while decimal_value != 0:
        hexValue = decimal_value%16
        hex = toHexChar(hexValue) + hex
        decimal_value = decimal_value//16

    return hex

def toHexChar(hexValue):
    if 0<= hexValue <= 9:
        return chr(hexValue +ord('0'))
    else:
        return chr(hexValue-10 +ord('A'))

def main():
    decimal_value = eval(input("Enter a decimal number: "))

    print("The hex number for decimal", decimal_value,"is",decimaltohex(decimal_value))

main()
        