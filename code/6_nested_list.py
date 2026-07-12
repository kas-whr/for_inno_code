# numbers = [10, 3]
# countries = ['Russia', 'Armenia', 'Argentina']
# info = ['Timur', 1992, 72.5]
#
# my_list = [[0], [1, 2], [3, 4, 5]]
#
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(len(my_list))
# Если требуется посчитать общее количество элементов во вложенном
# списке my_list , мы можем использовать цикл for в связке с функцией len() :


# my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik']]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# #
# #
# print(my_list[0][2]) # индексирование строки 'Python'
# print(my_list[1][1]) # индексирование списка [10, 20, 30]
# print(my_list[2][-1]) # индексирование списка ['Beegeek', 'Stepik!']
# print(my_list[2][-1][-1]) # индексирование строки 'Stepik!'
#
#
# #
# list1 = [1, 7, 12, 0, 9, 100]
# list2 = [1, 7, 90]
# list3 = [1, 10]
# print(min(list1, list2, list3))
# print(max(list1, list2, list3))
#
#
# list4 = [['a', 'b'], ['a'], ['d', 'p', 'q']]
# print(min(list4))
# print(max(list4))
#
#
# my_list = [[1, 7, 12, 0, 9, 100], ['a', 'b']]
# print(min(my_list))
# print(max(my_list))
#
#
# # методы все работают так же
#
#
#
#
# # Создание вложенных списков
# print([0] * 8)
# n, m = int(input()), int(input()) # считываем значения n и m
# my_list = []
# for _ in range(n):
#     my_list.append([0] * m)
# print(*my_list, sep='\n')
#
#
# n, m = int(input()), int(input()) # считываем значения n и m
# my_list = [[0]*m for _ in range(n)]
# print(my_list)
#
#
#
#

n = 4 # количество строк (элементов)
my_list = []
for _ in range(n):
    elem = [int(i) for i in input().split()] # создаем список из элементов строки
    my_list.append(elem)

print(my_list)

n = 4
my_list = []
for _ in range(n):
    elem = [int(i) for i in input().split()]
    my_list.extend(elem)

print(my_list)