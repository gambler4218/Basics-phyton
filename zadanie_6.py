with open('uch_plan.txt', 'r', encoding='utf-8') as uch_plan:
    i = 0
    for line in uch_plan:
        string = line.split()
        predmet = string[0].strip(':')
        prac = string[2].strip('(пр)').replace('-', '0')
        lec = string[1].strip('(л)').replace('-', '0')
        lab = string[3].strip('(лаб)').replace('-', '0')
        hours = int(lab) + int(prac) + int(lec)
        spisok = {predmet: hours}
        print(spisok)