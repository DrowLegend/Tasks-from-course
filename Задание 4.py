#В одномерном массиве все отрицательные элементы переместить в начало, а остальные в конец массива с сохранением порядка следования. Дополнительный массив не использовать.

def task_4(lis):
    i = 0
    length = len(lis)

    while i < length:
        if lis[i] < 0:
            lis.append(lis[i])
        i += 1

    i = 0
    while i < length:
        if lis[i] >= 0:
            lis.append(lis[i])
        i += 1

    print(lis[length:])


l = [-6, 2, 0, 5, -10, 2, -3, -5, 8, 9]
task_4(l)


