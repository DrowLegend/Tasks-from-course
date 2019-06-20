#поиск минимального и максимального числа в двумерном массиве

a = [[6, 4, 10], [5, 16, 11]]
elem_min = a[0][0]
elem_max = 0
for row in a:
    for elem in row:
        if elem < elem_min:
            elem_min = elem
        elif elem > elem_min:
            elem_min = elem_min
        if elem > elem_max:
            elem_max = elem
        elif elem < elem_max:
            elem_max = elem_max
#b = a.index(row)
z = a[1].index(elem_max)
v = a[0].index(elem_min)
a[1][z] = a[0][v]
a[0][v] = a[1][z]
print(a)
print(elem_min, elem_max)
print(z)
