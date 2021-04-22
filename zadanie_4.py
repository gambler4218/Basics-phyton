user = input()
word = user.split()

i = 0
n = 1

while i < int(len(word)):
    s = word[i][0:10]
    print(f'{n}: {s}')
    i +=1
    n +=1