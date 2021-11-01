def valores_negativos(arr):
    arr_neg = []
    for i in range(len(arr)):
        if arr[i] <= 0: 
            arr_neg.append(arr[i])
    return arr_neg
arr = [1,2,3,-1,-4,2,-6,5]
print(valores_negativos(arr))

