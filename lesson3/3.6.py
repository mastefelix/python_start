text = input('Введите слова маленькими латинскими буквами: ')


def int_func():
    if text.islower() and ascii(text)[1:-1].isalpha():
        return text.title()
    else:
        return 'При вводе разрешено использовать только маленькие латинские символы!'


print(int_func())
