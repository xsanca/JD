#Сортировки
#Курмачева А.А. группа 05-804
def insert_sort(A): #Функция сортировки вставками
    N = len(A) # вычисление длины массива А
    for i in range(1, N):
        k = i-1
        while k > -1 and A[k] > A[k+1]:
            A[k], A[k+1] = A[k+1], A[k] #меняет местами рядом стоящие элементы
            k -= 1
    return A
def choise_sort(A): #Функция сортировки выбором
    #сортировка в подмассивах , ищем локальные минимумы
    N = len(A)
    for i in range(N):
        topmin = i
        for k in range(i+1, N):#постоянно ищет минимум, затем меняет его с началом подсписка, далее начинает со следующего элемента не проверяя первый
            if A[topmin] > A[k]:
                A[topmin], A[k] = A[k], A[topmin]
    return A
def bubble_sort(A): #Функция сортировки пузырьком
    N = len(A)
    for top in range(N): #по общему количеству элементов
        i = top
        for k in range(1, N-i): #до отсортированной части
            if A[k-1] > A[k]:
                A[k-1], A[k] = A[k], A[k-1]
    return A

#A = [5, 4, 3, 2, 1]
n = int(input())
A = [] # создание списка
for i in range(n):
    c = float(input())
    A.append(c)
    B = A[:]
    C = A[:]
    D = A[:]
print(A)
print("Insert sort")
print(insert_sort(B))
print("Choise sort")
print(choise_sort(C))
print("Bubble sort")
print(bubble_sort(D))