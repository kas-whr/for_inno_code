# to do: 3, 5, 6, 8, 9, 10*, 11*

# TASK 1
n = int(input())
n2 = n
while n != 0:
    print("[", end="")
    n -= 1


while n2 != 0:
    print("]", end="")
    n2 -= 1

# TASK 2
a = ""
count = 0
while True:
    a = int(input())
    if a == 0:
        break
    count += 1
print(count)


# TASK 3
a = int(input())
sum = 0
while a != 0:
    sum += a # sum = sum + a
    a = int(input())

print(sum)





# 5
# n = int(input())
# i = 2
# while True:
#     if n % i == 0:
#         print(i)
#         break
#     i += 1

# print(i)


# 6
# a = int(input())
# max_num = a
# while a != 0:
#     if a > max_num:
#         max_num = a
#     a = int(input())
#
# print(max_num)


# 10
# a = 1
# b = 1
# n = int(input())
# i = 2
# while i < n:
#     c = a + b
#     a = b
#     b = c
#     i += 1
# print(b)

