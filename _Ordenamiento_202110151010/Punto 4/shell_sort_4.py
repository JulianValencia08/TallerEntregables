def shell_sort(arr):
    len_arr = len(arr)
    h = len_arr // 2
    while h > 0:
        for i in range(h, len_arr):
            t = arr[i]
            j = i
            while j >= h and arr[j - h] > t:
                print(arr[j], "->" ,arr[j - h])
                arr[j] = arr[j - h]
                j -= h
            print(arr[j], "->" , t)    
            arr[j] = t
        h = h // 2
        
        print(arr)
 
 
inp = [8, 47, 17, 6, 40, 16, 18, 97, 11, 7]
print("Pasadas")
shell_sort(inp)
print('Array after Sorting:')
print(inp)