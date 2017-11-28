# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

# ag = [3, 4, 5, 6, 7]
# for i in ag:
#     i = i * 2
#     ag[i] = i
#     print(ag)

ag = [3, 4, 5, 6, 7]
for v in range(5):
    ag[v] = ag[v] * 2
print(ag)