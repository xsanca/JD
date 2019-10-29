#Покрытие точек отрезками
#Дано множество n точек на прямой
#Найти минимальное количество отрезков единичной длин, которыми можно покрыть все точки
#Курмачева А.А. группа 05-804
list = [] #список, хранящий все введенные точки
lp = [] #список, хранящий левые концы отрезков
n = int(input()) #количество точек которые мы введем
for i in range(n): #заполнение списка с помощью цикла
    c = float(input()) #ввод элемента с клавиатуры
    list.append(c) #добавление элемента в список
list.sort() #сортируем по возрастанию
print(list) #вывод отсортированного списка введенных точек
i =int (0)
while i < n:
    lp.append(list[i])
    i += 1
    while i < n and list[i] <= (lp[-1] + 1):#идем по циклу пока длина отрезка не будет больше одного(начинаем с крайней левой точки)
        i += 1
print("Полученныe отрезки для покрытия:")
for a in lp:
        print(a, a + 1)
print("Количество отрезков:", len(lp))#Выводит длину списка, который хранил отрезки покрытия
