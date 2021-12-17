class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_data(cls, date_1):
        d, m, y = date_1
        return cls(int(d), int(m), int(y))

    @staticmethod
    def get_valid(obj):
        return True if 0 < obj.day < 32 and 0 < obj.month < 13 and obj.year == 2021 else False


d_1 = '07-12-2021'
date = Date.set_data(d_1.split('-'))
print(date.day)
print(date.month)
print(date.year)
print(Date.get_valid(date))
