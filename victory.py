import random

game = 'Да'

people = {'Пушкин': '06.06.1799'
    , 'Гоголь': '20.03.1809'
    , 'Лермонтов': '15.10.1814'
    , 'Толстой': '09.09.1828'
    , 'Тургенев': '09.11.1818'
    , 'Сталин': '18.12.1878'
    , 'Ленин': '22.04.1870'
    , 'Бах': '21.03.1685'
    , 'Моцарт': '27.01.1756'
    , 'Брежнев': '19.12.1906'}
months = {'01': 'январь'
    , '02': 'февраль'
    , '03': 'март'
    , '04': 'апрель'
    , '05': 'май'
    , '06': 'июнь'
    , '07': 'июль'
    , '08': 'август'
    , '09': 'сентябрь'
    , '10': 'октябрь'
    , '11': 'ноябрь'
    , '12': 'декабрь'}
words = {
    '06': 'шестое'
    , '20': 'двадцатое'
    , '15': 'пятнадцатое'
    , '09': 'девятое'
    , '18': 'восемнадцатое'
    , '22': 'двадцать второе'
    , '21': 'двадцать первое'
    , '27': 'двадцать седьмое'
    , '19': 'девятнадцатое'}
while game == 'Да':
    right = 0
    error = 0
    result = random.choices(list(people.keys()), k=5)
    print(result)
    for elem in result:
        date_born = input(f'Введите дату рождения {elem} формате "dd.mm.yyyy" :')
        if date_born != people[elem]:
            day, month, year = people[elem].split('.')
            print(f'Правильный ответ : {words[day]} {months[month]} {year} года')
            error += 1
        else:
            right += 1


    print('количество правильных ответов:', right)
    print('количество ошибок:', error)
    print('процент правильных ответов:', round((right * 100) / 5))
    print('процент неправильных ответов:', round((error * 100) / 5))
    game = input('Играем еще?:')
