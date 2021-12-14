class MyOwnErr(ValueError):
    def __init__(self, text):
        self.text = text


a = input('For continue enter number, for exit enter "stop": ')
my_list = []

while a != 'stop':
    try:
        if not a.isdigit():
            raise MyOwnErr('Only numbers!')
        a = int(a)
    except MyOwnErr as err:
        print(err)
    else:
        my_list.append(a)
    a = input('For continue enter number, for exit enter "stop": ')


print(my_list)
