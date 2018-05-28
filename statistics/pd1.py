def factorial(n):
    if n == 0:
        fat = 1
    else:
        fat = n
        while n > 1:
            fat *= factorial(n - 1)
            break
    return fat

l = float(input())
k = int(input())

P = (l ** k * 2.71828 ** -l) / factorial(k)
        
print("%.3f" %P)
