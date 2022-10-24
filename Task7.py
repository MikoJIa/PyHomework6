
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