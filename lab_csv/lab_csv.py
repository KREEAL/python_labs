'''
['Николаевна', 'Анна', '', '', 'evenko.73@mail.ru', 'Завершено', '19 Сентябрь 2017  17:07', '19 Сентябрь 2017  17:13', '6 мин. 17 сек.', '8,00', '1,00', '0,00', '1,00', '1,00', '0,00', '1,00', '1,00', '1,00', '1,00', '1,00']\

{'Фамилия': 'Ирина', 'Имя': 'Псалом', 'Учреждение (организация)': '', 'Отдел': '', 'Адрес электронной почты': 'Irina1991Psalom@yandex.ru', 'Состояние': 'Завершено', 'Тест начат': '21 Сентябрь 2017  21:34', 'Завершено': '21 Сентябрь 2017  21:42', 'Затраченное время': '8 мин. 12 сек.', 'Оценка/10,00': '8,00', 'В. 1 /1,00': '1,00', 'В. 2 /1,00': '1,00', 'В. 3 /1,00': '1,00', 'В. 4 /1,00': '1,00', 'В. 5 /1,00': '0,00', 'В. 6 /1,00': '1,00', 'В. 7 /1,00': '1,00', 'В. 8 /1,00': '1,00', 'В. 9 /1,00': '1,00', 'В. 10 /1,00': '0,00'}


Найти количество людей, выполнивших тест более чем за заданное время и набравших
ровно заданное количество баллов. Вывести их список в алфавитном порядке.
'''

import csv


def time_parser(timest):
    seps = timest.split(".")
    seconds = 0
    for sep in seps:
        if "дн" in sep:
            seconds += int(sep.split()[0]) * 24 * 60 * 60
        elif "час" in sep:
            seconds += int(sep.split()[0]) * 60 * 60
        elif "мин" in sep:
            seconds += int(sep.split()[0]) * 60
        elif "сек" in sep:
            seconds += int(sep.split()[0])
    return seconds

def float_maker(almost_number):
    return float(almost_number.split(",")[0])

def check_good_guy(guy_dict, marked_time, result_need):
    if(guy_dict['Состояние'] == "Завершено") and (time_parser(guy_dict['Затраченное время']) > marked_time):
        if 'Оценка/10,00' in guy_dict:
            return (float_maker(guy_dict['Оценка/10,00']) == float(result_need))
        else:
            return (float_maker(guy_dict['Оценка/100,00']) == float(result_need*10))



rows = []

time_compl = input("Введите заданное время, в формате XX дн.  YY час. ZZ мин. WW сек.\n")
marked_time = time_parser(time_compl.strip())
result_need = float(input("Введите заданное кол-во баллов (целое число 0 - 10)\n"))

good_guys = set()

with open("15_1.csv", encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=",")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'Файл сожержит столбцы: {",".join(row)}')
        else:
            if check_good_guy(row, marked_time, result_need):
                good_guys.add(str(str(row['Фамилия'].capitalize()) +" "+str(row['Имя']).capitalize()))
        count += 1

print(good_guys)


with open("15_2.csv", encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=",")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'Файл сожержит столбцы: {",".join(row)}')
        else:
            if check_good_guy(row, marked_time, result_need):
                good_guys.add(str(str(row['Фамилия']) +" "+str(row['Имя'])))
        count += 1

print(good_guys)

print()
print("ИСКОМЫЕ ЗНАЧЕНИЯ:")
print(sorted(good_guys))