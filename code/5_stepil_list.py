# TASK 1
# n = int(input())
# p = range(1, n + 1)
# l = list(p)
# print(l)

# print(list(range(1, int(input()) + 1)))

# TASK 2


# TASK 4
# n = int(input())
# nums = []
# for _ in range(n):
#     num = [int(input())]
#     nums += num
#
# print(max(nums) + min(nums))

# TASK 7
n = int(input())
mas = []
for _ in range(n):
    num = [int(input())]
    mas += num

# mas = [5, 4, 3, 2, 1]
for i in range(len(mas)):
    for j in range(i + 1, len(mas)):
        if mas[i] > mas[j]:
            mas[i], mas[j] = mas[j], mas[i]
print(*mas)