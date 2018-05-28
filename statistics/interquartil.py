def medquart(lista):
    lista.sort()
    l2 = len(lista) / 2
    if len(lista) % 2 == 0:
        mediana = (lista[int(l2)] + lista[int(l2 - 1)]) / 2
        seg1 = lista[0:int(l2)]
        seg3 = lista[int(l2):]
    else:
        mediana = lista[int(l2 - 0.5)]
        seg1 = lista[0:(int(l2 - 0.5))]
        seg3 = lista[int(l2 + 0.5):]
    return mediana, seg1, seg3

n = int(input())
X = [int(x) for x in input().split()]
F = [int(f) for f in input().split()]
lisfin = []

for i in range(n):
    r = 0
    while r < F[i]:
        lisfin.append(X[i])
        r += 1
        
a, b, c = medquart(lisfin)
q1 = medquart(b)
q3 = medquart(c)
interq = q3[0] - q1[0]
print("%.1f" % interq)
