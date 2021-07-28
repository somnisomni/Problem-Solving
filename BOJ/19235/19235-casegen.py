import random

print(10000)
for i in range(10000):
    rand1 = random.randint(1, 3)

    if rand1 == 1:
        print(rand1, random.randint(0, 3), random.randint(0, 3))
    elif rand1 == 2:
        print(rand1, random.randint(0, 3), random.randint(0, 2))
    elif rand1 == 3:
        print(rand1, random.randint(0, 2), random.randint(0, 3))