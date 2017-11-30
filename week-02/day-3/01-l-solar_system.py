# Saturn is missing from the planet_list
# Insert it into the correct position

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]

planet_list = planet_list[:5] + ["Saturn"] + planet_list[5:]
print(planet_list)