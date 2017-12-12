from d1_e3_Domino import Domino

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...

# print(dominoes)

# FIRST TRY
# for domi in range(len(dominoes)):
#     # if dominoes[domi].values[1] == dominoes[domi - 1].values[0]:
#     for domiNum in dominoes[domi].values[]:
#         if domiNum == dominoes[domi+1].values[0]:
#             print('Success', dominoes[domi].values[1], dominoes[domi - 1].values[0])
#         else:
#             print('Hope') 
#     # if domi[1] == domi + 1[0]

# SOLUTION 1
# for i in range(len(dominoes) - 1):
#     for j in range(len(dominoes)):
#         if dominoes[i].values[1] == dominoes[j].values[0]:
#             temp = dominoes[i + 1]
#             dominoes[i + 1] = dominoes[j]
#             dominoes[j] = temp

# print(dominoes)

# SOLUTION 2
def sorter(list):
    new_dominoes = []
    new_dominoes.append(dominoes[0])
    while len(new_dominoes) != len(list):
        for i in range(1, len(dominoes)):
            if dominoes[i].values[0] == new_dominoes[-1].values[1]:
                new_dominoes.append(dominoes[i]) 
    return new_dominoes

print(sorter(dominoes))