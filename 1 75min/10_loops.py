for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, -1, -1):
    print(i)

for i in range(-10, -1, -1):
    print(i)

x = [3, 4, 42, 3, 2, 4]
for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i, element)

i = 0
while i < 10:
    print("run")
    i += 1

i = 0
while True:
    print("run")
    i += 1
    if i == 10:
        break
