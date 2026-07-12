# n = int(input())
# m = int(input())
#
# my_list = []
# for i in range(n):
#     inner = []
#     for j in range(m):
#         inner.append(input())
#
#     my_list.append(inner)
#
# for inner in my_list:
#     # inner = ['и', 'швец']
#     print(*inner) # и швец

# put your python code here

# TASK 2
n = int(input())
m = int(input())

my_list = []
for i in range(n):
    inner = []
    for j in range(m):
        inner.append(input())

    my_list.append(inner)

print(my_list)

# my_list = [['и', 'швец'], ['и', 'жнец'], ['и', 'на'], ['дуде', 'игрец']]
for i in range(n):
    for j in range(m):
        print(my_list[i][j], end=' ')
    print()

print()

for i in range(m):
    for j in range(n):
        print(my_list[j][i], end=' ')
    print()









# n = int(input())
# o = []
# for i in range(n):
#     m = int(input())
#     print(m)
#     x = (m * m) + (2 * m) + 1
#
# o.append(x)
# print()
# print(*o, sep=' \n')
# print(1, 2, 4, 5, sep='\n')