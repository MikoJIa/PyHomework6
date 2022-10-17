"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
# Первый вариант словаря!
dictionary = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна',
    6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень'   
}
user = int(input('Enter number - '))
print(f'Результат чере словарь: {dictionary[user]}')

# Второй вариант словаря!
dictionary = {'Зима': (1, 2, 12),
              'Весна': (3, 4, 5),
              'Лето': (6, 7, 8),
              'Осень': (9, 10, 11)}
 
user = int(input('Enter number - '))
for key in dictionary.keys():
    if user in dictionary[key]:
        print(key)

# Вариант решения через список!
lst = ['Зима', 'Весна', 'Лето', 'Осень']
#length = len(lst)
user = int(input('Enter number - '))
if user == 12 or user == 1 or user == 2:
    print(lst[0])
elif user == 3 or user == 4 or user == 5:
    print(lst[1])
elif user == 6 or user == 7 or user == 8:
    print(lst[2])
elif user == 9 or user == 10 or user == 11:
    print(lst[3])            