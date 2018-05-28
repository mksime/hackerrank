lista = input().split()
positive, negative = [int(z) for z in lista]

n = int(input()) #número de tentativas pra ter sucesso
p = positive / (positive + negative) #probabilidade de sucesso p/ 1 tentativa
q = 1 - p

g = q ** (n - 1) * p

# Probabilidade de sucesso nas n primeiras tentativas
#soma = 0
#for i in range(1, 6):
#    g = q ** (i - 1) * p
#    soma += g
#    
print("%.3f" %g)
