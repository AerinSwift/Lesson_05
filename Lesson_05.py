# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
import json

f = open("lines.txt", "w")
user_line = input("Введите строку, которая будет записана в файл. Для окончания - введите пустую строку.\n")
while user_line:
    f.writelines(user_line + '\n')
    user_line = input("Введите строку, которая будет записана в файл. Для окончания - введите пустую строку.\n")
    if not user_line:
        break
f.close()
print("Запись завершена.")

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


file_2 = open('lines.txt', 'r')
content = file_2.read()
print(f'Содержимое файла: \n {content}')
file_2 = open('lines.txt', 'r')
content = file_2.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('lines.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество слов в {i + 1} строке: {len(content[i].split())}')
file_2.close()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

print("Программа считывает данные из файла и выводит их.")
print("Также она отмечает сотрудников, у которых оклад менее 20000, и подсчитывает средний оклад по файлу.")

with open('employees.txt', 'r') as emp_file:
    salary = []
    under_payed = []
    emp_list = emp_file.read().split('\n')
    print(f'Содержимое файла: {emp_list}')
    for i in emp_list:
        i = i.split()
        if int(i[1]) < 20000:
            under_payed.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000: {under_payed}, средний оклад {round(sum(map(int, salary)) / len(salary), 2)}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_numbers = []
with open('eng_numbers.txt', 'r') as eng_file:
    for i in eng_file:
        i = i.split(' ', 1)
        rus_numbers.append(russian[i[0]] + '  ' + i[1])

with open('rus_numbers.txt', 'w') as rus_file:
    rus_file.writelines(rus_numbers)
print("На основании файла 'eng_numbers.txt' создан файл 'rus_numbers.txt'.")

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('summarization.txt', 'w+') as sum_file:
    user_numbers = input('Введите цифры через пробел \n')
    sum_file.writelines(user_numbers)
    numbers_in_file = user_numbers.split()
print(f'Сумма чисел в файле: {sum(map(int, numbers_in_file))}')

# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

subject_hours = {}
with open('subjects.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split('-')
        if not lecture:
            lecture = 0
        if not practice:
            practice = 0
        if not lab:
            lab = 0
        print(f'Предмет - {subject}: лек.-{lecture}, пр.- {practice}, лаб.-{lab}')
        subject_hours[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предметам: \n {subject_hours}')

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

profit = {}
pr = {}
prof = 0
average_profit = 0
i = 0
with open('statistics.txt', 'r') as file:
    for line in file:
        name, firm, earnings, damage = line.split()
        profit[name] = int(earnings) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    average_profit = prof / i
    print(f'Прибыль средняя - {average_profit:.2f}')

    pr = {'Средняя прибыль': round(average_profit)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('statistics.json', 'w') as stat_js:
    json.dump(profit, stat_js)
    print(f'Создан файл с расширением json')
