#Домашняя работа 2 ФИО:Михайлова Ксения
#1
geo_logs = [
['visit1', ['Москва', 'Россия']],
['visit2', ['Дели', 'Индия']],
['visit3', ['Владимир', 'Россия']],
['visit4', ['Лиссабон', 'Португалия']],
['visit5', ['Париж', 'Франция']],
['visit6', ['Лиссабон', 'Португалия']],
['visit7', ['Тула', 'Россия']],
['visit8', ['Тула', 'Россия']],
['visit9', ['Курск', 'Россия']],
['visit10', ['Архангельск', 'Россия']],
]

#в цикле добавляем значения в новый список, на выходе отфильтрованные значения
geo_logs_filtred = []

for i in geo_logs:
   tmp = i[1][1]
   if tmp !=  'Россия':
       pass
       #geo_logs.remove(i)

   else:
        geo_logs_filtred.append(i)

print(geo_logs_filtred)

#2
 ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}

#
 values = []

 for key in ids:
    for i in ids[key]:
        if not (i in values ):
            values.append(i)
        else:
            pass

 print(values)

#3
 queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]
cnt_queries = []
#считаем запросы с список
for query in queries:
    cnt_queries = (len(query.split()))

# создаем словарь с ключами количеством слов в запросе, а значение сколько раз встречается в списке, ключ 100 это общее количество запросов
result = {
    100 : 0
}

for i in cnt_queries:
    if i not in result:
     result.setdefault(i, 1)
     result[100] += 1
    else:
     result[i] += 1
     result[100] += 1

#расчитываем и выводим значения
 num = 0
 percent = 0
 for key, value in result.items():
   if key != 100:
    percent = value/result[100]*100
    num = int(key)
    print('Процент запросов {: .2f}% для количества слов {: d}'.format(percent, num))

#4
 stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

 # получаем в переменную название канала с максимальным объемом и выводим.
 max_channel = max(stats.keys(), key=(lambda x: stats[x]))
 print(max_channel)

#5
 stream = [
'2018-01-01,user1,3',
'2018-01-07,user1,4',
'2018-03-29,user1,1',
'2018-04-04,user1,13',
'2018-01-05,user2,7',
'2018-06-14,user3,4',
'2018-07-02,user3,10',
'2018-03-21,user4,19',
'2018-03-22,user4,4',
'2018-04-22,user4,8',
'2018-05-03,user4,9',
'2018-05-11,user4,11',
]

#вычисляем с помощью переменных в цикле значение и выводим
 tmp_user = ''
 count_users = 0
 count_watches = 0
 tmp = 0

 for line in stream:
    tmp = int(line.split(',')[2])
    count_watches += tmp
    if tmp_user != line.split(',')[1]:
      count_users += 1
      tmp_user = line.split(',')[1]
    else:
       pass

 print('Среднее значение просмотров на пользователя {: .2f}'.format(count_watches/count_users))

#6

stats = [
['2018-01-01', 'google', 25],
['2018-01-01', 'yandex', 65],
['2018-01-01', 'market', 89],
['2018-01-02', 'google', 574],
['2018-01-02', 'yandex', 249],
['2018-01-02', 'market', 994],
['2018-01-03', 'google', 1843],
['2018-01-03', 'yandex', 1327],
['2018-01-03', 'market', 1764],
]

date = '2018-01-01'
channel = 'google'
value = [line[2] for line in stats if (line[0] == date) and (line[1] == channel)]
print(value)
