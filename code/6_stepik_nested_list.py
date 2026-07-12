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

n = int(input())
o = []
for i in range(n):
    m = int(input())
    print(m)
    x = (m * m) + (2 * m) + 1

o.append(x)
print()
print(*o, sep=' \n')
print(1, 2, 4, 5, sep='\n')