def hex_equivalents(hex):
    if hex == 10:
        return "A"
    elif hex == 11:
        return "B"
    elif hex == 12:
        return "C"
    elif hex == 13:
        return "D"
    elif hex == 14:
        return "E"
    elif hex == 15:
        return "F"
    else:
        return hex

def from_decimal(decimal, system):
    number = decimal
    divisor = 2
    system_string = ""
    if system == "hex":
        divisor = 16
    elif system == "octal":
        divisor = 8

    while number > 0:
        raw_digit = number % divisor
        if system == "hex":
            raw_digit = hex_equivalents(raw_digit)
        system_string = f"{raw_digit}{system_string}"
        number //= divisor
        return system_string

def octal_to_decimal(octal):
    pass

def hex_to_decimal(hex):
    pass

def binary_to_decimal(binary):
    pass