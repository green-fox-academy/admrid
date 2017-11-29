
example = "In a dishwasher far far away"

# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away

# listword1[] = example[5:16]

example = example[:5] + "galaxy " + example[16:]

print(example)

