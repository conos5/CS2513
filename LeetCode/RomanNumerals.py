# Solution:


def romanToInt(s: str) -> int:

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0
    for value in s:
        if value not in roman_numerals:
            print("value not accepted; must be roman numeral")
        else:
            output += roman_numerals[value]
            return output


usr_input = input("Roman Numeral Input: ")
print(romanToInt(usr_input))