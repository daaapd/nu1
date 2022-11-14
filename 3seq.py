listComa1 = input('Введите любые цифры через запятую 1 список:')
listComa2 = input('Введите любые цифры через запятую 2 список:')
list1 = listComa1.split(',')
list2 = listComa2.split(',')
res = [ele for ele in list1]
print(res)
for a in list2:
    if a in list1:
        print(a)
        res.remove(a)
print('Результат:', ','.join(res))
