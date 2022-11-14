listComa = input('Введите любые цифры через запятую:')
list = listComa.replace(';',',').replace('/',',').split(',')
uniqList = []
for elem in list:
    if list.count(elem) == 1:
        uniqList.append(elem)

print('Рузультат:', ','.join(uniqList))
