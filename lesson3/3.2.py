def my_func():
    name = input('Имя: ').title()
    surname = input('Фамилия: ').title()
    year = input('Год рождения: ')
    city = input('Город проживания: ').title()
    email = input('Email: ')
    phone = input('Телефон: ')
    return f'{name} {surname} {year} года рождения. Проживает в городе {city}. Контакты для связи: {email}, {phone}'


print(my_func())
