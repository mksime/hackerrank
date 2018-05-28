def medquart(lista):
    lista.sort()
    l2 = len(lista) / 2
    if len(lista) % 2 == 0:
        mediana = (lista[int(l2)] + lista[int(l2 - 1)]) / 2
        seg1 = X[0:int(l2)]
        seg3 = X[int(l2):]
    else:
        mediana = lista[int(l2 - 0.5)]
        seg1 = X[0:(int(l2 - 0.5))]
        seg3 = X[int(l2 + 0.5):]
    return mediana, seg1, seg3

n = 9
#n = int(input())
X = [3, 7, 8, 5, 12, 14, 21, 13, 18]
#X = [int(x) for x in input().split()]

a, b, c = medquart(X)
q1 = medquart(b)
q3 = medquart(c)
#print(medquart(X)[0])# isso funciona tb
print(int(q1[0]))
print(int(a))
print(int(q3[0]))
