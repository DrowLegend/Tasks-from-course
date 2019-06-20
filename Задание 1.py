#метод, который возвращает True or False если в одномерном массиве имеются три подряд идущих одинаковых элемента

def true_or_false(massiv):
    i = 1
    index = 1
    t = 0
    while i < len(massiv):
        if massiv[i] == massiv[i - index]:
            t = True
            break
        if massiv[i] != massiv[i - index]:
            t = False
            i += 1
            continue

    if t == True:
        return True
    elif t == False:
        return False





mass1 = [1, 2, 3, 5, 5, 5, 5, 6]
mass2 = [1, 4, 6, 7, 9, 0]
mass3 = [1, 1, 2, 5, 6, 8, 8, 8, 8]

print(true_or_false(mass3))