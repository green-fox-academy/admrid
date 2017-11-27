# Create a program that writes this line 100 times:
# "I won't cheat on the exam!"

print("They like The Simpsons so:" )

bart = "I won't cheat on the exam!"

n = 0

while n <= 100:
    print(bart)
    n += 1

for n in range(0, 100):
    print(str(n) + ".", bart)