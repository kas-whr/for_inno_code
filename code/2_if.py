# 1
# sx = int(input())
# sy = int(input())
#
# fx = int(input())
# fy = int(input())
#
# if (sx == fx or sy == fy) or (abs(fx - sx) == abs(fy - sy)):
#     print("YES")
# else:
#     print("NO")

# 2
# xs = int(input())
# ys = int(input())
# xf = int(input())
# yf = int(input())

# if abs(xf - xs) <= 1 and abs(yf - ys) <= 1:
#     print("YES")
# else:
#     print("NO")

# 3
# year = int(input())
#
# if (year % 4 == 0 and not(year % 100 == 0)) or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")


#
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
