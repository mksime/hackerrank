from math import sqrt

N = int(input())
X = [int(x) for x in input().split()]

num = 0 #numerador
soma = 0 #denominador

for i in range(N):
    soma += X[i]
    
mean = soma / N

for i in range(N):
    num += (X[i] - mean) ** 2
    
sd = sqrt(num / N)

print("%.1f" % sd)
