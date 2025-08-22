def from_decimal(decimal, system):
    hex_map = "0123456789ABCDEF"
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
            raw_digit = hex_map[raw_digit]
        system_string = f"{raw_digit}{system_string}"
        number //= divisor
        return system_string

def octal_to_decimal(octal):
    pass

def hex_to_decimal(hex):
    pass

def binary_to_decimal(binary):
    pass