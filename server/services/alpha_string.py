from fastapi import HTTPException, status
from typing import Tuple

VALUE_ROMAN_CHARACTERS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

ROMAN_LETTERS = ["I", "V", "X", "L", "C", "D", "M"]

def isroman(number: str) -> bool:
    """
    Check if roman patter is obeyed
    """
    for letter in ROMAN_LETTERS:
        if letter*4 in number:
            return False
    return True

def roman2decimal(number: str) -> int:
    if number:
        if not isroman(number):
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY)
        try:
            return VALUE_ROMAN_CHARACTERS[number]
        except KeyError:
            return sum([
                VALUE_ROMAN_CHARACTERS[single_number]
                for single_number in number
            ])

def find_max_roman_number(alpha_string: str) -> Tuple[str, int]:

    list_numbers = []
    roman_number = ""
    max_number = 0
    max_value = ""

    for idx, alpha in enumerate(alpha_string):
        if alpha in VALUE_ROMAN_CHARACTERS:
            roman_number += alpha
            if idx < len(alpha_string) - 1:
                continue
        if roman_number:
            print(roman_number)
            decimal_number = roman2decimal(roman_number)
            if decimal_number > max_number:
                max_number = decimal_number
                max_value = roman_number
            roman_number = ""
    return max_value, max_number
