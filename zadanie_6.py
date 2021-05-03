from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

c = 0
a = [1, 2, 5]
for i in cycle(a):
    if c > 10:
        break
    print(i)
    c +=1