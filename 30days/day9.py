#Recursão
#fatorial recursivo

def factorial(n):
    if n == 0:
        fat = 1
    else:
        fat = n
        while n > 1:
            fat *= factorial(n - 1)
            break
    return fat

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
