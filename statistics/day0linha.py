import numpy as np

N = int(input())
X = [int(x) for x in input().split()]
W = [int(w) for w in input().split()]

#Modo com numpy
mean_weight = np.average(X, weights = W)

#sem numpy
num = 0 #numerador
dem = 0 #denominador

for i in range(N):
    num += (X[i] * W[i])
    dem += W[i]

mean_weight = num / dem

print("%.1f" % mean_weight)
