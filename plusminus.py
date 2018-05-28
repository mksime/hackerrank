def plusMinus(arr):
    #
    # Write your code here.
    #
    plus = 0
    minus = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            plus += 1
        elif arr[i] < 0:
            minus += 1
        else:
            zero += 1
    pf = plus / len(arr)
    mf = minus / len(arr)
    zf = zero / len(arr)
    print("%.6f\n %.6f\n %.6f" % (pf, mf, zf))

lista = [-4, 3, -9, 0, 4, 1]
plusMinus(lista)
