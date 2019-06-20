#поиск чисел в массиве сумма которых равна указанной(25) и возвращает их индексы

class L:
    def two_sum(self, arr, res):
        for i in arr:
            for j in arr:
                if i + j == res:
                    return arr.index(i), arr.index(j)


ar = [3, 10, 17, 8, 9, 31]

l = L()
print(l.two_sum(ar, 25))