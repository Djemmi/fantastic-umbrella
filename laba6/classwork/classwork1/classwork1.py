with open('classwork1.txt', encoding='utf8') as file:
    for line in file:
        line.replace(" ", "")
        line = line.split(';')
        print('%s|%s получил(а) оценку %s' %(line[0], line[1], line[2]) )
