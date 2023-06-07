#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        nums = []
        myDict = {"X": 10, "V": 5, "I": 1, "L": 50, "D": 500, "C": 100}
        for l in roman_string:
            for s in myDict:
                if s == l:
                    nums.append(myDict.get(s))
        return nums

    else:
        return None
