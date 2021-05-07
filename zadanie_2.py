with open('slova.txt') as doc:
    i = 0
    for line in doc:
        i += 1
        string = len(line.split())
        print(f'В строке {i} - {string} слов')