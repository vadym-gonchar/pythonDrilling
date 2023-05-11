def print_formatted(number):
    l = len(bin(number).lstrip('0b')) + 1
    for i in range(1, number + 1):
        result = ''
        decimal = str(i).rjust(l - 1)
        octal = str(oct(i)).lstrip('0o').rjust(l)
        hexal = str(hex(i)).lstrip('0x').upper().rjust(l)
        binary = str(bin(i)).lstrip('0b').rjust(l)
        result += decimal + octal + hexal + binary
        print(result)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
