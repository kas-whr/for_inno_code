# n = 8
# numbers = [1, 2, 5, 6, 8]
# names = ["Lena", 'Vasya']
# info = ["Petya", 16]
#
# print(numbers[2])
# print(numbers[-1])
# print(names[0])
# print(numbers[:3])

# nums = []
# names = list()
# print(nums)
# print(names)

# name = "Ali \nna"
# syms_name = list(name)
# print(name)
# print(syms_name)
#
# print(list(range(1, 6, 2)))


# numbers = [1, 2, 5, 6, 8]
# names = ["Lena", 'Vasya']
# print(len(numbers))
# print(len(names))
#
# print(2 in numbers)
# print(2 not in numbers)
# print(0 not in numbers)
#
#
#
# name = "Lena"
# print(name.upper())
# print(name)

# error
# name[2] = "O"
# print(name)


# nums = [1, 2, 3, 4, 5, 6]
# print(nums)
#
# nums[1:4] = [10, 11, 12]
# print(nums)
#
# names = ["Lena", "Vasya"] + ["Lena", "Vasya"] = ["Lena", "Vasya", "Lena", "Vasya"]
# print(names + nums)
# print(names * 3)


# считывание n строк
# n = input()
# for _ in range(n): # 0 1 2 3
#     a = input()
#

# считывание строк до условия
# a = input()
# while a != "0":
#     a = input()


# сортировка пузырьком
# mas = [5, 4, 3, 2, 1]
# for i in range(len(mas)):
#     for j in range(i + 1, len(mas)):
#         if mas[i] > mas[j]:
#             mas[i], mas[j] = mas[j], mas[i]
# print(mas)
#
# n = int(input())
# mas = []
# for _ in range(n):
#     num = [int(input())]
#     mas += num
#
# # mas = [5, 4, 3, 2, 1]
# for i in range(len(mas)):
#     for j in range(i + 1, len(mas)):
#         if mas[i] > mas[j]:
#             mas[i], mas[j] = mas[j], mas[i]
# print(mas)

# n = 5
# for i in range(n): # 0 1 2 3 4 5 ... n-1
#     print("Привет")




# METHODS
# append()
# numbers = [1, 1, 2, 3, 5, 8, 13] # создаем список
# numbers.append(21) # добавляем число 21 в конец списка
# numbers.append(34) # добавляем число 34 в конец списка
# print(numbers)
#
# numbers = [] # создаем список
# numbers.append(21) # добавляем число 21 в конец списка
# numbers.append(34) # добавляем число 34 в конец списка
# print(numbers)

# не можем использовать индексаторы для установки значений
# элементов списка, если такого индекса нет
# numbers[0] = 1 # OK
# numbers[1] = 2 # OK
# print(numbers)
# numbers[1] = 3 # error: list assignment index out of range
# print(numbers)
#
# # extend()
# numbers = [0, 2, 4, 6, 8, 10]
# odds = [1, 3, 5, 7]
# numbers.extend(odds)
# print(numbers)
#
#
# # difference extend() / append()
# words1 = ['iq option', 'stepik', 'beegeek']
# words2 = ['iq option', 'stepik', 'beegeek']
# words1.append('python')
# words2.extend('python')
# #
# print(words1) # ['iq option', 'stepik', 'beegeek', 'python']
# print(words2) # ['iq option', 'stepik', 'beegeek', 'p', 'y', 't', 'h', 'o', 'n']
#
#
# # del - ОПЕРАТОР (не метод)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[5] # удаляем элемент имеющий индекс 5
# print(numbers)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[2:7] # удаляем элементы с 2 по 6 включительно
# print(numbers)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[::2]
# print(numbers)
#
#
# # Вывод
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(numbers)):
#     print(numbers[i])
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num, end=' ')
#
#
# print(*numbers)
# print(*numbers, sep='\n')
# print(*numbers, sep='-')
#
# # распаковка строк
# s = 'Python'
# print(*s)
# print()
# print(*s, sep='\n')

#
#
# # split()
# s = 'Python is the most powerful language'
# words = s.split()
# print(words)
#
# numbers = input().split()
# print(numbers)
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# print(numbers)
#
#
# ip = '192.168.1.24'
# numbers = ip.split('.') # указываем явно разделитель
# print(numbers)
# #
# # # разница между s.split() и s.split(' ')
# s = 'Python     is the       most powerful language'
# words1 = s.split()
# words2 = s.split(' ')
# print(words1)
# print(words2)
# #
# #
# #
# # # join()
# words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
# s = ' '.join(words)
# print(s)
#
#
# words = ['Мы', 'учим', 'язык', 'Python']
# print('*'.join(words))
#
#
# # split(), join() являются строковыми методами



#insert
# names = ['Gvido', 'Roman' , 'Timur']
# print(names)
# names.insert(1, 'Anders')
# print(names)
# names.insert(3, 'Josef')
# print(names)

# index
# names = ['Gvido', 'Roman', 'Timur']
# position = names.index('Timur')
# print(position)
# # position = names.index('Anders')
#
# if 'Anders' in names:
#     position = names.index('Anders')
#     print(position)
# else:
#     print('Такого значения нет в списке')
#
# # remove() - первый элемент, значение которого равняется переданному в метод значению
# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# del food[1]
# print(food)
# food.remove('Рис')
# print(food)
#
# # pop() - удаляет элемент по указанному индексу и возвращает его
# names = ['Gvido', 'Roman' , 'Timur']
# item = names.pop(1)
# print(item)
# item = names.pop()
# print(item)
# print(names)
#
# # count()
# names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
# cnt1 = names.count('Timur')
# cnt2 = names.count('Gvido')
# cnt3 = names.count('Josef')
# print(cnt1)
# print(cnt2)
# print(cnt3)
#
# # reverse()
# names = ['Gvido', 'Roman' , 'Timur']
# names.reverse()
# print(names)
#
# # Метод reverse() меняет порядок
# # элементов на обратный в текущем списке, а срез создает копию списка
# names = ['Gvido', 'Roman' , 'Timur']
# reversed_names = names[::-1]
# print(names)
# print(reversed_names)
# names.reverse()
# print(names)
#
# # clear()
# names = ['Gvido', 'Roman' , 'Timur']
# names.clear()
# print(names)
#
# # copy()
# names = ['Gvido', 'Roman' , 'Timur']
# names_copy = names.copy() # создаем поверхностную копию списка names
# print('orig', names)
# print('copy', names_copy)

# names_copy.append("Petya")
# print('orig', names)
# print('copy', names_copy)
#


# списочные выражения
# numbers = []
# for i in range(10):
#     if i % 2 == 0:
#         numbers.append(i)
#
# print(numbers)
# numbers = [i*2 for i in range(10) if i % 2 == 0]
#
# print(numbers)
