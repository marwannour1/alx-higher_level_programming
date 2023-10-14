#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return (0)
    roman_dict = {'I': 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    total = 0
    previous = -1
    for letter in reversed(roman_string):
        if roman_dict[letter] >= previous:
            total += roman_dict[letter]
        else:
            total -= roman_dict[letter]

        previous = roman_dict[letter]
    return (total)
