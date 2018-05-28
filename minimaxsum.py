def miniMaxSum(arr):
    #
    # Write your code here.
    #
    soma = 0
    for i in arr:
        soma += i
    return soma - max(arr), soma - min(arr)
    
l = [1, 2, 3, 4, 5]
print(miniMaxSum(l))
