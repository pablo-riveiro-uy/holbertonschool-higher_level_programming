#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score = 0
        for key in a_dictionary:
            if a_dictionary.get(key) is None:
                return None
            if a_dictionary.get(key) > score:
                score = a_dictionary.get(key)
                winner = key
        return winner
    else:
        return None
