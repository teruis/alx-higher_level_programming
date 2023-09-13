#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value
    """
    if not a_dictionary:
        return None

    max_key = None
    max_score = float('-inf')
    for key, value in a_dictionary.items():
        if value > max_score:
            max_key = key
            max_score = value

    return max_key
