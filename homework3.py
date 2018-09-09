#Домашняя работа 2 ФИО:Михайлова Ксения

#1
data = [
[13, 25, 23, 34],
[45, 32, 44, 47],
[12, 33, 23, 95],
[13, 53, 34, 35],
]

#Функция возвращает сумму элементов на диагонали
def sum_diagonal (alist):
    num = 0
    result = 0
    count = 0
    for line in alist:
        num = line[count]
        result = result + num
        count += 1

    return result

sum_diagonal (data)

#2
data = [1, '5', 'abc', 20, '2']

#функция возвращает сумму квадратов элементов, которые могут быть числами.
def sum_num_square(alist):
    result = 0
    num = 0
    square = 0
    for i in alist:
        if type(i) is int:
            num = i
        else:
            if str.isnumeric(i):
                num = int(i)
        square = num*num
        result = result + square
        square = 0
        num = 0
    return result

sum_num_square(data)

#3
#функция возвращает название валюты (поле 'Name') с максимальным значением курса с помощью сервиса https://www.cbr-xml-daily.ru/daily_json.js
import requests

 def name_for_max_value():
        max_value = 0
        name = ''
        tmp = 0
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        get_data = r.json()['Valute']
        for key, value in get_data.items():
            valute = value
            if max_value < valute['Value']:
                    max_value = valute['Value']
                    name = valute['Name']

        print(name)

name_for_max_value()

#4

class Rate:
#4.2 Добавлен в класс параметр diff (со значениями True или False)
    def __init__(self, format='value', diff=False):
        self.format = format
        self.diff = diff

    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:

        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }

        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                return response[currency]['Value']

#4.1 Добавлен в класс еще один формат, который возвращает название валюты (например, 'Евро').
            if self.format == 'name':
                return response[currency]['Name']
        return 'Error'

    def get_diff(self, currency):
         response = self.exchange_rates()

         if currency in response:
                value = response[currency]['Value']
                prev = response[currency]['Previous']
                result = prev - value
                return result

    def eur(self,diff=False):
        if diff == False:
       # """Возвращает курс евро на сегодня в формате self.format"""
               return self.make_format('EUR')
        else:
        #"""Возвращает изменение по сравнению в прошлым значением курса евро"""
            return self.get_diff('EUR')

    def usd(self,diff=False):
        if diff == False:
        #"""Возвращает курс доллара на сегодня в формате self.format"""
              return self.make_format('USD')
        else:
       # """Возвращает изменение по сравнению в прошлым значением курса доллара"""
            return self.get_diff('USD')

#5
#функция возвращающую сумму первых n чисел Фибоначчи
def fibonnachi (num):
        a = 0
        b = 1
        for __ in range(num):
            a, b = b, a + b
        return a

fibonnachi (10)


#6
#функция преобразующую произвольный список вида ['2018-01-01', 'yandex', 'cpc', 100] в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
data = ['2018-01-01', 'yandex', 'cpc', 100]

def list_to_dict (alist):
        cnt = 0
    len_list = len(alist)
    for i in alist:
        if cnt != len_list - 1:
            if cnt == 0:
                dict.setdefault(i, {})
            elif cnt == 1:
                indx = alist[cnt - 1]
                dict[indx].setdefault(i, {})
            elif cnt == 2:
                indx = alist[cnt - 1]
                indx0 = alist[cnt - 2]
                value = alist[cnt + 1]
                dict[indx0][indx].setdefault(i, value)

        elif i == len_list:
            pass
        cnt = cnt + 1

list_to_dict (data)

print(dict)        
