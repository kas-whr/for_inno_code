# to do: 1, 2, 3, 5, 6, 7, 8, 9

# TASK 1
# variant 1
print("Я - программист!")
print("Я - программист!")
print("Я - программист!")

# variant 2
# text = "Я - программист!"
# print(text)
# print(text)
# print(text)


# TASK 2
print("I", "like", "Python", sep="***")


# TASK 3
separator = input()
str1 = input()
str2 = input()
str3  = input()
print(str1, str2, str3, sep=separator)


# TASK 4
str1 = input()
str2 = input()
str3  = input()
print(str3, str2, str1)


# TASK 5
# variant 1
x = int(input())
y = int(input())
print(x + y)

# varinat 2
# x = input()
# y = input()
# x = int(x)
# y = int(y)
# print(x + y)

# variant 3
# x = input()
# y = input()
# print(int(x) + int(y))


# TASK 6
n = int(input()) # friends
k = int(input()) # pizza
print(k // n)


# TASK 7
n = int(input()) # friends
k = int(input()) # pizza
print(k % n)


# TASK 8
n = int(input())
print(n % 10)


# TASK 9
n = int(input())
print(n // 10)


# TASK 10
n = int(input())
x = n % 10
n //= 10
y = n % 10
n //= 10
z = n % 10
print(x + y + z)


# TASK 11
cost_rub = int(input())
cost_cop = int(input())
n = int(input())

res_rub = cost_rub * n
res_cop = cost_cop * n

# а если копеек > 100?
res_rub += res_cop // 100
res_cop %= 100
print(res_rub, res_cop)
