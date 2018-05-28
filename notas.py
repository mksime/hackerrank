from random import randint

def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
    a = 0
    b = 0
    listA = [a0, a1, a2]
    listB = [b0, b1, b2]
    for i in range(len(listA)):
        if listA[i] > listB[i]:
            a += 1
        elif listA[i] < listB[i]:
            b += 1
    return a, b
    #print(a, b)

a0 = randint(1,101)
a1 = randint(1,101)
a2 = randint(1,101)
b0 = randint(1,101)
b1 = randint(1,101)
b2 = randint(1,101)

print(a0, a1, a2, b0, b1, b2)
print(solve(a0, a1, a2, b0, b1, b2))
