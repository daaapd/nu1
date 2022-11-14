count = input('Введите количество элементов:')
count = int(count)
list = []
for i in range(count):
    temp=input('Введите ' + str(i) + ' элемент:')
    list.append(temp)
list.sort()
print('Вывод:', list)
