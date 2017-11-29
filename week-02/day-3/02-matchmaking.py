# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]
order = []

# for i in girls:
#     order += [i] 

order.append(girls[0])
order.append(boys[0])
order.append(girls[1])
order.append(boys[1])
order.append(girls[2])
order.append(boys[2])

for i in range(len(boys)):
    if i <= 4:
        order.append(girls[i])
        order.append(boys[i])
    else:
        order.append(boys[i])

print(order)