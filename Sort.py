#Сортировки
#Курмачева А.А. группа 05-804
def insert_sort(A): #Функция сортировки вставками
    N = len(A) # вычисление длины массива А
    for top in range(1, N):
        k = top-1
        while k > -1 and A[k] > A[k+1]:
            A[k], A[k+1] = A[k+1], A[k]
            k -= 1
    return A;
def choise_sort(A): # Функция сортировки выбором
    N = len(A)
    for top in range(N):
        topmin = top
        for k in range(top+1, N):
            if A[topmin] > A[k]:
                A[topmin], A[k] = A[k], A[topmin]
    return A;
def bubble_sort(A): # Функция сортировки пузырьком
    N = len(A)
    for top in range(N):
        i = top
        for k in range(1, N-i):
            if A[k-1] > A[k]:
                A[k-1], A[k] = A[k], A[k-1]
    return A;

#A = [5, 4, 3, 2, 1]
n = int(input())
A = [] # создание списка
for i in range(n):
    c = float(input())
    A.append(c)
print(A)
print("Insert sort")
print(insert_sort(A))
print("Choise sort")
print(choise_sort(A))
print("Bubble sort")
print(bubble_sort(A))