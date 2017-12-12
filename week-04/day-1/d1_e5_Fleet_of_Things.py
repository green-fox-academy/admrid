from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

print(fleet)

def fleetMaker():
    listitem1 = Thing("Get Milk")
    listitem2 = Thing("Remove the obstacles")
    listitem3 = Thing("Stand up")
    listitem3.complete()
    listitem4 = Thing("Eat lunch")
    listitem4.complete()
    fleet = Fleet()
    fleet.add(listitem1)
    fleet.add(listitem2)
    fleet.add(listitem3)
    fleet.add(listitem4)
    return fleet

print(fleetMaker())