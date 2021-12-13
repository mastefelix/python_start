class MyOwnErr(ValueError):
    def __init__(self, text):
        self.text = text


a = input('For continue enter number, for exit enter "stop": ')
my_list = []

while a != 'stop':
    try:
        a = int(a)
    except ValueError:
        print('Only numbers!')
    else:
        my_list.append(a)
    a = input('For continue enter number, for exit enter "stop": ')


print(my_list)
