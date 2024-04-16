def convert_to_base_n(number, base):
    if not isinstance(number, int) or not isinstance(base, int):
        raise ValueError("Both number and base must be integers")
    if number < 0 or base < 2:
        raise ValueError("Number must be non-negative and base must be greater than 1")

    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number //= base

    return result if result else "0"

print(convert_to_base_n(36, 3))