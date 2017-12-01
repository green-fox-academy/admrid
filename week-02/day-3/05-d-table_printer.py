# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]

# MANUAL PRINT FUNCTION TO UNDERSTAND HOW IT WORKS
# def printer(table):
# 	length1 = len(table[3]["name"]) #18
# 	length2 = 13
# 	length3 = 8
# 	print(' +' + '-' * (length1 + 2) + '+' + '-' * (length2 + 2) + '+' + '-' * (length3 + 2) + '+')
# 	print(' | ' + 'Ingredients' + ' ' * (length1 - len('Ingredients')) + ' | ' + 'Needs cooling' + ' | ' + 'In stock'  + ' | ')
# 	print(' +' + '-' * (length1 + 2) + '+' + '-' * (length2 + 2) + '+' + '-' * (length3 + 2) + '+')
# 	print(' | ' + table[0]['name'] + ' ' * (length1 - len(table[0]['name'])) + ' | ' + 'Yes' + ' ' * (length2 - len('Yes')) + ' | ' + str(table[0]["in_stock"]) + ' ' * (length3 - len(str(table[0]["in_stock"]))) + ' | ')
# 	print(' | ' + table[1]['name'] + ' ' * (length1 - len(table[1]['name'])) + ' | ' + 'Yes' + ' ' * (length2 - len('Yes')) + ' | ' + str(table[1]["in_stock"]) + ' ' * (length3 - len(str(table[1]["in_stock"]))) + ' | ')
# 	print(' | ' + table[2]['name'] + ' ' * (length1 - len(table[2]['name'])) + ' | ' + 'Yes' + ' ' * (length2 - len('Yes')) + ' | ' + str(table[2]["in_stock"]) + ' ' * (length3 - len(str(table[2]["in_stock"]))) + ' | ')
# 	print(' | ' + table[3]['name'] + ' ' * (length1 - len(table[3]['name'])) + ' | ' + 'Yes' + ' ' * (length2 - len('Yes')) + ' | ' + str(table[3]["in_stock"]) + ' ' * (length3 - len(str(table[3]["in_stock"]))) + ' | ')
# 	print(' | ' + table[4]['name'] + ' ' * (length1 - len(table[4]['name'])) + ' | ' + 'Yes' + ' ' * (length2 - len('Yes')) + ' | ' + str(table[4]["in_stock"]) + ' ' * (length3 - len(str(table[4]["in_stock"]))) + ' | ')
# 	print(' | ' + table[5]['name'] + ' ' * (length1 - len(table[5]['name'])) + ' | ' + 'Yes' + ' ' * (length2 - len('Yes')) + ' | ' + str(table[5]["in_stock"]) + ' ' * (length3 - len(str(table[5]["in_stock"]))) + ' | ')
# 	print(' | ' + table[6]['name'] + ' ' * (length1 - len(table[6]['name'])) + ' | ' + 'Yes' + ' ' * (length2 - len('Yes')) + ' | ' + str(table[6]["in_stock"]) + ' ' * (length3 - len(str(table[6]["in_stock"]))) + ' | ')
# 	print(' | ' + table[7]['name'] + ' ' * (length1 - len(table[7]['name'])) + ' | ' + 'Yes' + ' ' * (length2 - len('Yes')) + ' | ' + str(table[7]["in_stock"]) + ' ' * (length3 - len(str(table[7]["in_stock"]))) + ' | ')
# 	print(' +' + '-' * (length1 + 2) + '+' + '-' * (length2 + 2) + '+' + '-' * (length3 + 2) + '+')


def printer(table):
	length1 = len(table[3]['name']) #18
	length2 = 13
	length3 = 8
	for i in range(len(table)):
		if table[i]['needs_cooling'] == True:
			table[i]['needs_cooling'] = 'Yes'
		else:
			table[i]['needs_cooling'] = 'No'
	for i in range(len(table)):
		if table[i]['in_stock'] == 0:
			table[i]['in_stock'] = '-'
	print(' +' + '-' * (length1 + 2) + '+' + '-' * (length2 + 2) + '+' + '-' * (length3 + 2) + '+')
	print(' | ' + 'Ingredients' + ' ' * (length1 - len('Ingredients')) + ' | ' + 'Needs cooling' + ' | ' + 'In stock'  + ' | ')
	print(' +' + '-' * (length1 + 2) + '+' + '-' * (length2 + 2) + '+' + '-' * (length3 + 2) + '+')
	for i in range(len(table)):
		print(' | ' + table[i]['name'] + ' ' * (length1 - len(table[i]['name'])) + ' | ' + table[i]['needs_cooling'] + ' ' * (length2 - len(table[i]['needs_cooling'])) + ' | ' + str(table[i]["in_stock"]) + ' ' * (length3 - len(str(table[i]["in_stock"]))) + ' | ')
	print(' +' + '-' * (length1 + 2) + '+' + '-' * (length2 + 2) + '+' + '-' * (length3 + 2) + '+')

printer(ingredients)






