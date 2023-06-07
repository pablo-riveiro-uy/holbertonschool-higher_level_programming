#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        nums = []
        myDict = {"X": 10, "V": 5, "I": 1, "L": 50,
                  "D": 500, "C": 100, "M": 1000}
        for c in roman_string:
            for s in myDict:
                if s == c:
                    nums.append(myDict.get(s))
        added = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                added += nums[i] - nums[i - 1] * 2
            else:
                added += nums[i]
        return added
    else:
        return None
