#!/usr/bin/python3
def roman_to_int(roman_string: str) -> int:
    if not isinstance(roman_string, str):
        return 0

    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    number = 0
    for i in range(len(roman_string) - 1):
        if roman[roman_string[i]] < roman[roman_string[i + 1]]:
            number -= roman[roman_string[i]]
        else:
            number += roman[roman_string[i]]

    return number + roman[roman_string[-1]]


if __name__ == "__main__":
    roman = "DCXXI"
    print(roman_to_int(roman))
