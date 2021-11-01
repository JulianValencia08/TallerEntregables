def delete_same_elements_ordenatedvec(list):
    arr = []
    for i in list:
        if i not in arr:
            arr.append(i)
    return arr
list = [1,1,2,3,4,5,6,7,7,8,8,9,9]
print(delete_same_elements_ordenatedvec(list))