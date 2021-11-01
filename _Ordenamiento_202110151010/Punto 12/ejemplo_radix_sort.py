def radixsort(MyList):
  n = len(MyList)
  max = MyList[0]
  for i in MyList:
    if max < i:
      max = i
  place = 1
  while max/place > 0:
    countingsort(MyList, place)
    place *= 10  
def countingsort(MyList, place):
  n = len(MyList)
  output = [0 for i in range(0,n)]
  freq = [0 for i in range(0,10)]
  for i in range(0,n):
    freq[(MyList[i]//place)%10] += 1
  for i in range(1,10):
    freq[i] += freq[i - 1]      
  for i in range(n-1,-1,-1):
    output[freq[(MyList[i]//place)%10] - 1] = MyList[i] 
    freq[(MyList[i]//place)%10] -= 1
  for i in range(0,n): 
    MyList[i] = output[i]   
def PrintList(MyList):
  for i in MyList:
    print(i, end=" ")
  print("\n") 
                 
MyList = [101, 1, 20, 50, 9, 98, 27, 153, 35, 899]
print("Original List")
PrintList(MyList)

radixsort(MyList)
print("Sorted List")
PrintList(MyList)