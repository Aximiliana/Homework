#Домашняя работа 1 ФИО:Михайлова Ксения
#1
long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
print(len(long_phrase) > len(short_phrase))

#2
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
count_a = ((len(text) - len(text.replace('а',""))) / len('а'))
count_b = ((len(text) - len(text.replace('и',""))) / len('и'))
print (count_a > count_b)

#3
bytes = 213.68
mega = (bytes/1024)
'Объем файла равен: {: .2f}Mb'.format(mega)

#4
import math
math.sin(math.radians(30))

#5
print(0.1 + 0.2)

#6
a = 12
b = 43
a = a + b
b = a - b
a = a - b
print(a,b)

#7
# Перевод в десятичную через степень двойки:
# делаем число строкой, реверс чтобы верно определить что идет в итоговую сумму, цикл с вычислением
num = 10011
tmp = str(num)
tmp = tmp[::-1]
n = len(tmp)
out = 0
for i in range(n):
    two = 2 **i
    col = int(tmp[i])
    if col == 1:
     out = out + two
    else:
      pass
print(out)
