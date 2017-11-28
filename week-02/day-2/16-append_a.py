# - Create a variable named `nimals`
#   with the following content: `["kuty", "macsk", "cic"]`
# - Add all elements an `"a"` at the end

nimals = ["kuty", "macsk", "cic"]
for v in range(3):
    nimals[v] = nimals[v] + "a"
print(nimals)