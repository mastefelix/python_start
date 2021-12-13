class MyOwnErr(ZeroDivisionError):
    def __init__(self, text):
        self.text = text


a, b = input('Enter number: '), input('Enter number: ')

try:
    a, b = int(a), int(b)
    if b == 0:
        raise MyOwnErr('You cannot divide by zero!')
except (ValueError, MyOwnErr) as err:
    print(err)
