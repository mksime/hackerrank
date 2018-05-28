def fatorial(f):
    fat = 1
    if f == 0:
        fat = 1
    else:
        for i in range(f, 0,  -1):
            fat = fat * i
    return fat

lista = input().split()
positive, negative = [int(z) for z in lista]
#boy, girl = [1, 1]

p = positive / (positive + negative)
q = 1 - p
n = 6
x = 3
soma = 0
for r in range(x, 7): #o range muda de acordo com o modo como se organizam os resultados desejados. "Pelo menos x" -- (0, x + 1). "No mínimo x" -- (x, n + 1)
    b = (fatorial(n) / (fatorial(r) * fatorial(n - r))) * (p ** r) * (q ** (n - r))
    soma += b
print(soma)
