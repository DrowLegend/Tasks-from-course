#поиск наибольшего и наименьшего элемента прямоугольной матрицы и поменять их местами

def matrix(mat):
    print("Оригинальная матрица")
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()
    print("")
    #Поиск минимального и максимального значения
    elem_min = mat[0][0]
    elem_max = 0
    for row in mat:
        for elem in row:
            if elem < elem_min:
                elem_min = elem
            elif elem > elem_min:
                elem_min = elem_min
            if elem > elem_max:
                elem_max = elem
            elif elem < elem_max:
                elem_max = elem_max


    #Поиск индекса строки
    i = 0
    index_row_min = 0
    while i < len(mat):
        if elem_min in mat[i]:
            index_row_min = mat.index(mat[i])
            #print(index_row_min)
            break
        i += 1
        continue
    i = 0
    index_row_max = 0
    while i < len(mat):
        if elem_max in mat[i]:
            index_row_max = mat.index(mat[i])
            #print(index_row_max)
            break
        i += 1
        continue

    #Поиск индекса элемента в строке
    index_elem_min = 0
    if elem_min in mat[index_row_min]:
        index_elem_min = mat[index_row_min].index(elem_min)
        #print(index_elem_min)
    index_elem_max = 0
    if elem_max in mat[index_row_max]:
        index_elem_max = mat[index_row_max].index(elem_max)
        #print(index_elem_max)

    #Замена минимального и максимального местами
    mat[index_row_min][index_elem_min] = elem_max
    mat[index_row_max][index_elem_max] = elem_min

    #Печать матрицы
    print("Измененная матрица")
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()
    print(" ")

    print("Минимальный элемент матрицы %d" % elem_min)
    print("Максимальный элемент матрицы %d" % elem_max)


a = [[1, 4, 10], [5, 9, 11], [7, 3, 9]]
b = [[63, 4, 2], [4, 2, 0], [45, 3, 10], [1, 6, 90]]


matrix(b)






