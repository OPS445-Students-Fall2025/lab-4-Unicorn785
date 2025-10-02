#!/usr/bin/env python3
# Author ID: pkandasamy7@myseneca.ca

#if theres no characters in 0-9 it will return false, if there is it would be true
def is_digits(sobj):
    #Return True if all characters in sobj are digits, otherwise False
    for ch in sobj:
        if ch not in '0123456789':
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
