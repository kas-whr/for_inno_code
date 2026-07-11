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


n = int(input())
nums = []
for i in range(n):
    a = [int(input())]  # [9]
    nums += a # [8] + [9] = [8, 9]

# []







