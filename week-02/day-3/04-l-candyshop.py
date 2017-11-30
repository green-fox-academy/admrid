shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list. 
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)

# ez is jo:
# wrong1 = shop_items.index(2)
# wrong2 = shop_items.index(False)

# shop_items[wrong1] = "Croissant"
# shop_items[wrong2] = "Ice cream"

#type(i) megadja a tipusat
# def itemfinder():
#     for i in shop_items:
#         print(type(i))
#         if type(i) == "str":
#             print("yes")
#     print("oh")

# itemfinder()

for i in range(len(shop_items)):
    if shop_items[i] == 2:
        shop_items[i] = 'Croissant'
    elif shop_items[i] == False:
        shop_items[i] = 'Ice cream'

print(shop_items)

#shop_items.index()