import json
with open('firma.txt', 'r', encoding='utf-8') as firma:
    spisok = []
    for line in firma:
        string = line.split()
        price = int(string[2])
        rashod = int(string[3])
        prib = price - rashod
        #дальше не знаю как