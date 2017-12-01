# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1 
#
# - Print this two dimensional list to the output

# li = [[1, 0, 0, 0,], [0, 1, 0, 0,], [0, 0, 1, 0,], [0, 0, 0, 1,] ]
# print(li)

# li = []
# for r in range(4):
#     li.append([])
#     for j in range(4):
#         li[r].append(0)
#         print(li)


# l = [1, 0, 0, 0]

# for i in range(4):
#     print(l)
#     l[i]=0
#     l[i+1]=1

# print(l)

n = [0, 0, 0, 0]
for i in range(0, len(n)):
    n[i] = 1
    n[i-1] = 0
    print(*n, sep=' ')

