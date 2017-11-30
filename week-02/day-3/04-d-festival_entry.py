watchlist = []

security_alcohol_loot = 0

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

cango = []
watchlist = []

# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

def sec(lista): 
    global security_alcohol_loot  
    for listitem in lista:
        if listitem['guns'] > 0 and listitem['alcohol'] > 0:
            listitem['guns'] = 0
            watchlist.append(listitem['name'])
        if listitem['alcohol'] > 0 and listitem['guns'] == 0:
            security_alcohol_loot += listitem['alcohol']
            listitem['alcohol'] = 0
            cango.append(listitem)

sec(queue)
print(cango)