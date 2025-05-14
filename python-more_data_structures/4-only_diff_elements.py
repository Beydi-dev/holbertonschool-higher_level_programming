#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_1 = set_1 - set_2
    diff_2 = set_2 - set_1
    new_set = set()
    return (set_1 | set_2) - (set_1 & set_2)
