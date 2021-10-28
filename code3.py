import random

b = []
count = 0
while True:
    a = random.randint(0, 1000)
    b.append(a)
    count +=1
    if count == 1000:
        break
c = set(b)
print(c)