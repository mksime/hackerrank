#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(len(arr))
for i in range(-1, (len(arr) * -1) -1, -1):
    print(arr[i], end = ' ')
