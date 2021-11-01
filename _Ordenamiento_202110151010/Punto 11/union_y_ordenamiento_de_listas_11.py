def quicksort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return quicksort(izquierda)+ centro + quicksort(derecha)
    else:
      return lista
a = []
b = []
c = []
for i in range(100):
    a.append(i)
    if i <= 60:
        b.append(i)

quicksort(a)
quicksort(b)
c = a + b
print(quicksort(c))



