game = 'Да'

while game == 'Да':
    right = 0
    error = 0
    bornYear = input('Год рождения А.С Пушкина?:')  # 1799
    if bornYear == '1799':
        right += 1
    else:
        error += 1
    bornYear = input('Год рождения Николай Гоголь?:')  # 1809
    if bornYear == '1809':
        right += 1
    else:
        error += 1
    bornYear = input('Год рождения Николай М.Ю. Лермонтов?:')  # 1814
    if bornYear == '1814':
        right += 1
    else:
        error += 1
    bornYear = input('Год рождения Николай Иван Тургенев?:')  # 1818
    if bornYear == '1818':
        right += 1
    else:
        error += 1
    bornYear = input('Год рождения Николай Лев Толстой?:')  # 1828
    if bornYear == '1828':
        right += 1
    else:
        error += 1
    print('количество правильных ответов:', right)
    print('количество ошибок:', error)
    print('процент правильных ответов:', round((right * 100) / 5))
    print('процент неправильных ответов:', round((error * 100) / 5))
    game = input('Играем еще?:')
