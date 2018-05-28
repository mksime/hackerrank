#matrizes
#hourglass
#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
#no exemplo, a matriz é:
#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 2 4 4 0
#0 0 0 2 0 0
#0 0 1 2 4 0

hgfinal = -64 #pq esse problema é sacana

for i in range(4):
    for j in range(4):
        hg = 0
        hg += arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
        print(hg, hgfinal)
        if hg > hgfinal:
            print("Entrei no if")
            hgfinal = hg
    
print(hgfinal)
