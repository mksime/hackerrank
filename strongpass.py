#!/bin/python3

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    n = 0
    l = 0
    u = 0
    s = 0
    total = 0
    ml = 0
    for i in password:
        if i in numbers:
            n = 1
        elif i in lower_case:
            l = 1
        elif i in upper_case:
            u = 1
        elif i in special_characters:
            s = 1
    total = 4 - (n + l + u + s)
    ml = 6 - len(password)
    if total == 4 and ml <= 0:
        return "Strong"
    elif total > ml:
        return total
    else:
        return ml


if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
