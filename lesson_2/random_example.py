import random

random.seed(1)

print(random.choice(range(100)))
print(random.choice(range(100)))
print(random.choice(range(100)))
print(random.choice(range(100)))

for i in range(100):
    random.seed(i)
