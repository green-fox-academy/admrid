# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs

verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

# def create_new_verbs(verbs, preverb):
def create_new_verbs():
    newverbs = []
    for verb in verbs:
        newverbs.append(preverb + verb)
    print(newverbs)

create_new_verbs()


# for verb in verbs:
#     print(verb)

# for index in range(len(verbs)):
#     print(verbs[index])
