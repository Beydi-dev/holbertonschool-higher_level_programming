#!/usr/bin/python3
def uniq_add(my_list=[]):
    found = []
    result = 0
    for i in my_list:
        if i not in found:
            found.append(i)
            result += i
    return result
