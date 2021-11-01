def delete_same_elements(list):
    arr = []
    for i in list:
        if i not in arr:
            arr.append(i)
    return arr
list = [4,7,11,4,9,5,11,7,3,5]
print(delete_same_elements(list))
