
from functools import reduce
# перемножить нечётные числа друг с другом
lst = [x for x in range(1, 6, 2)]
res = reduce(lambda item, item2: item * item2, lst )
print(res)
# Необходимо сроку 'hello' вывести наоборот
def solution(string):
    return string[::-1]
res = solution('hello')
print(res)
# сделать срез первого элемента и последнего
def remove(s):
    res = s[1:-1]
    return res
a = remove('yourwoter')
print(a)
# надо поссчитать количество очков нашей команды:
# if x>y = 3points 
# if x>y = 0points  
# if x==y = 1points 
def point(games):
    count = 0
    for i in games:
        scores_str = i.split(':')
        first_score = int(scores_str[0])
        second_score = int(scores_str[1])
        if first_score > second_score:
            count += 3
        elif first_score == second_score:
            count += 1
    return count
res = point(['1:0', '2:0','3:0','4:0','5:0','5:1','5:2'])
print(res)

# Найти чмсло в масиве за 7 ходов
# В этой функции мы перебирае каждый элемент и сравниваем с item
def binary_search(list, item):
    low = 0                        #  В low и high хронятся границы той части где будет производится поиск
    high = len(list) - 1
    while low <= high:             # Пока эта часть не сократится до одного элемента...
        mid = (low + high)         # ...проверяем средний элемент
        guess = list[mid]
        if guess == item:          # Значение найдено
            return mid
        if guess > item:           # Если больше чем item...
            high = mid - 1         # ...то мы high присваиваем mid - 1
        else:                      # Мало
            low = mid + 1
    return None                # Мало

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


def selectionsort(arr):
    new_arr = []
    smallest = arr[0]
    for i in range(len(arr)):
       
        if arr[i] < smallest:
            smallest = arr[i]
            #new_arr.append(arr.pop(smallest))
    return smallest
print(selectionsort([5, 3, 6, 7, 8, 2, 10, 4, 11]))

# Убрать один восклицательный знак в конце строки
# remove('Hi!') => 'Hi'
# remove('Hi!!!') => 'Hi!!'
# remove('Hi! Hi!') => 'Hi! Hi'
def remove(s):
    length = len(s)
    for i in range(length-1, -1, -1):
        print(s[i])
        if s[i] == '!':
            s = s[0:-1]
            return s
        else:
            return s
    #s = s.replace('!', ' ')
res = remove('Hi!!!')
print(res)

# Дан список с числами, необходимо вернуть список из двух элементов где первый элемент
# это сумма положительных чисел, а второй элемент сумма отрицательных чисел
# ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
def count_positives_sum_negatives(arr):
    positive_count = 0
    negative_count = 0
    if not arr:
        return []
    for i in arr: # пробегаемся по всем элементам списка
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_count += i
    return [positive_count, negative_count]

res = count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
print(res)

# Дано число n, необходимо вернуть количество положительных нечётных чисел.

def odd_count(n):
    count = 0
    while n > count:
        for i in range(1, n):
            if i % 2 != 0:
                count += 1
        return count
print(odd_count(15023))

# Необходимо найти строку иголка в списке и вернуть строку в которой говорится, что игла найдена в позиции....
# (found the needle at position  5)

# Первый способ решения!!!!

def find_needle(haystack):
    for i in haystack:
        if 'needle' in i:
            index = haystack.index('needle')
    return print(f'found the needle at position {index}')

# Второй способ решения!!!!

def find_needle(haystack):
    return 'found the needle at position {}'.format(haystack.index('needle'))
# Третий способ решения!!!!

def find_needle(haystack):
    index = 0
    for i in haystack:
        if i == 'needle':
            return f"found the needle at position {index}"
        index += 1

res = find_needle(['hay', 'junk', 'hay', 'hay', 'morejunk', 'needle', 'randomjunk'])
print(res)

# Необходимо взять строку с именем и сделать инициалы в верхнем регистре
# Пример: Sam Harris => S.H
# Пример: sam harris => S.H

def abbrev_name(name):
    result_string = name.split()[0][:1].capitalize() + '.' + name.split()[1][:1].capitalize()
    return result_string

def abbrev_name(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

def abbrev_name(name):
    first_initial = name[0]
    for letter in range(len(name)):
        if name[letter] == ' ':
            last_initial = name[letter + 1]
    return (first_initial.upper() + '.' + last_initial.upper())
res = (abbrev_name('Sam Harris'))
print(res)

def palindrom(string):
    revesed_str = string[::-1]
    if revesed_str.lower() == string.lower():
        return True
    else:
        return False

def is_palindrome(s):
    if s.lower() == s[::-1].lower():
        return True
    else:
        return False

def is_palindrome(s):
    s = s.lower()
    return s[::-1] == s

res = palindrom('abba')
print(res)