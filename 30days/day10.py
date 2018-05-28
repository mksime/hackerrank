#!/bin/python3

import sys


n = int(input().strip())
binario = bin(n)[2:]
if n == 0:
    contgeral = 0
else:
    cont = 1
    contgeral = 1
    for d in range(1, len(binario)):
        while binario[d] == str(1) and binario[d - 1] == str(1):
            cont += 1
            d += 1
            if d >= len(binario):
                break
        if cont >= contgeral:
            contgeral = cont
            cont = 1
        elif cont < contgeral:
            cont = 1
        
print(contgeral)
