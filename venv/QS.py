# Курмачева А.А. 05-804
# быстрая сортировка
import random
def Quick_Sort(A):
    if len(A) <= 1:#чтобы не проверять одноэлементные списки
        return A
    else:
        c = random.choice(A)#выбирает рандомное число из A
        K = []
        L = []#три списка для хранения чисел меньше, больше и равных с
        R = []
        for i in A:#проверяем каждое число из списка
            if i < c:#когда число меньше
                K.append(i)
            elif i > c:#когда число больше
                L.append(i)
            else:#для случаев, когда равно
                R.append(i)
        return Quick_Sort(K) + R + Quick_Sort(L)
A=[1,7,5,8,4]
print(A)
print("Отсортированный: ", Quick_Sort(A))
