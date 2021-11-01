def search_in_matriz(arr, x):
    for i in range(len(arr)):
        for j in arr[i]:
            if arr[i][j] == x:
                return "Si"
            else:
                return "No"    


matriz = [[1,2,2,2,3,4],[1,2,3,3,4,5],[3,4,4,4,4,6],[4,5,6,7,8,9]]
print(search_in_matriz(matriz,20))