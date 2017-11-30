# - Create a variable named `aj`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements in `aj`
# - Print the elements of the reversed `aj`

aj = [3, 4, 5, 6, 7]
# rj = 0
# for i in range(len(aj) - 1, -1, -1):
#     rj.append(i)
# print(aj = rj)

aj[4], aj[3], aj[2], aj[1], aj[0] = aj[0], aj[1], aj[2], aj[3], aj[4]
print(aj)

# OR:
# ja = []

# for i in aj[::-1]:
#     ja.append(i)
# aj = ja
# print(aj)