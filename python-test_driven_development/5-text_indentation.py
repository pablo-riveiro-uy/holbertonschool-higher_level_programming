#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    
    enter = False
    separators = ['.','?',':']
    for letter in text:
        if letter == " " and enter:
            continue
        enter = False
        if letter not in separators:
           print(letter, end="")
        else:
            print(letter)
            print()
            enter = True