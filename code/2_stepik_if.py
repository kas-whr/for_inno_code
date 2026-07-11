# to do: 4 - 10

# TASK 1
password1 = input()
password2 = input()
if password1 == password2:
    print("Пароль принят")
else:
    print("Пароль не принят")


# TASK 2
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)


# TASK 3
a = int(input())
b = int(input())
c = int(input())
if a >= b >= c or a >= c >= b:
    print(a)
elif b >= a >= c or b >= c >= a:
    print(b)
else:
    print(c)


# TASK 4
a = int(input())
b = int(input())
c = int(input())
if (a + b) > c and (a + c) > b and (c + b) > b:
    print("YES")
else:
    print("NO")


# TASK 5
xs = int(input())
ys = int(input())
xf = int(input())
yf = int(input())
if xs == xf or ys == yf:
    print("YES")
else:
    print("NO")


# TASK 6
xs = int(input())
ys = int(input())
xf = int(input())
yf = int(input())
if xs == xf or ys == yf or (abs(xf - xs) == abs(yf - ys)):
    print("YES")
else:
    print("NO")


# TASK 7
xs = int(input())
ys = int(input())
xf = int(input())
yf = int(input())
if abs(xf - xs) <= 1 and abs(yf - ys) <= 1:
    print("YES")
else:
    print("NO")


# TASK 8
n = int(input())
m = int(input())
k = int(input())
if (k % n == 0 or k % m == 0) and n * m > k:
    print("YES")
else:
    print("NO")


# TASK 9
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")


# TASK 10
a = int(input())
b = int(input())
sym = input()

if sym == "+":
    print(a + b)
elif sym == "-":
    print(a - b)
elif sym == "*":
    print(a * b)
elif sym == "/" and b == 0:
    print("На ноль делить нельзя!")
elif sym == "/":
    print(a / b)
else:
    print("Неверная операция")