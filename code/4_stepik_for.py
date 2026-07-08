# n = int(input())
# line = "*" * 19
# for i in range(n):
#     print(line)

# 5, 1: 5, 4, 3, 2, 1

m = int(input())
n = int(input())

if m < n:
    for i in range(m, n + 1):
        print(i)

if m > n:
    for i in range(m, n - 1, -1):
        print(i)



