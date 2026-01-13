                            # Задачи на кортежи
# 1
tup = (2, 3, 6, 3, 1, 2, 7, 4, 3, 9)
max_t = max(tup)
min_t = min(tup)
print(max_t - min_t)

# 2
tup = (2, -3, 6, -3, 1, 2, 7, 4, 3, -9)
change_1 = 0
for i in range(1, len(tup)):
    if tup[i] > 0 and tup[i-1] < 0 or tup[i] < 0 and tup[i-1] > 0:
        change_1 += 1
print(change_1)

# 3
up = (25, 34, 67, -31, 11, 23, 76, 43, 32, 92)
for i in range(len(tup)):
    deliteli = 0
    for j in range(1, abs(tup[i])):
        if abs(tup[i]) % j == 0:
            deliteli += 1
    if deliteli == 1:
        print(tup[i])

# 4
tup = (5, 2, 6, 8, 9, 7, 5, 7, 8) #O(1)
count_max = 0 #Кол-во элементов максимальной последовательности
count_1 = 0 #Кол-во элементов возрастающей последовательности
count_2 = 0 #Кол-во элементов убывающей последовательности
first_index = 0
for i in range(len(tup) - 1):
    if tup[i] < tup[i + 1]:
        count_1 += 1
        if count_1 + 1 > count_max:
            count_max = count_1 + 1
            first_index = i - count_1 + 1
    else:
        count_1 = 0
    if tup[i] > tup[i + 1]:
        count_2 += 1
        if count_2 + 1 > count_max:
            count_max = count_2 + 1
            first_index = i - count_2 + 1
    else:
        count_2 = 0
print(count_max)
print(tup[first_index: first_index + count_max])
# 5
tup = (1, 2, 1, 2, 6, 1, 2)
for i in range(len(tup)):
    count_1 = 0
    r_count = 0
    for k in range(i):
        if tup[k] == tup[i]:
            r_count += 1
    if r_count > 0:
        continue
    for j in range(i + 1, len(tup)):
        if tup[j] == tup[i]:
            count_1 += 1
    if count_1 > 0:
        print(tup[i])

                        # Задачи на списки
# 1
lst_1 = [4, 1, 6 ,9]
lst_2 = [8, 1, 2, 4, 9, 5, 7, 6]
while lst_1:
    min_1 = min(lst_1)
    if min_1 in lst_2:
        lst_1.remove(min_1)
    else:
        print(min_1)
        break
else:
    print('Нет такого элемента')

# 2
lst_1 = [1, 2, 1, 4, 1,6]
lst_2 = lst_1.copy()
count_1 = 0
for i in range(len(lst_1)):
    if int(lst_1[i]) % 2 == 0:
        count_1 += 1
        number_1 = int(lst_1[i])
        str_1 = ''
        index_1 = i + count_1
        while number_1:
            number_2 = number_1 % 10
            number_1 = number_1 // 10
            str_1 += str(number_2)
        number_1 = int(str_1)
        lst_2.insert(index_1, number_1)
print(lst_2)

# 3
lst_1 = [5, 2, 4, 5, 1, 2]
lst_2 = lst_1.copy()
while lst_2:
    for i in range(max(lst_1) + 1):
        if i in lst_2:
            count_1 = lst_2.count(i)
            print(i, '-', count_1, end=' ')
            while i in lst_2:
                lst_2.remove(i)

# 4
lst_1 = [5, 2, 0, -2, -7, 1, 8, 0, -1]
lst_2 = lst_1.copy()
lst_3 = lst_1.copy()
count_1 = 0
while lst_2:
    for i in range(len(lst_1)):
        if lst_1[i] > 0:
            lst_2.remove(lst_1[i])
            continue
        elif lst_1[i] < 0:
            lst_3.append(lst_1[i])
            lst_3.remove(lst_1[i])
            lst_2.remove(lst_1[i])
        else:
            count_1 += 1
            lst_2.remove(lst_1[i])
            lst_3.remove(lst_1[i])
while count_1:
    lst_3.append(0)
    count_1 -= 1
print(lst_3)

# 4
lst_1 = [5, 2, 0, -2, -7, 1, 8, 0, -1]
count_1 = 0
count_2 = 0
len_1 = len(lst_1)
for i in range(len_1):
    if lst_1[i - count_2] > 0:
        continue
    elif lst_1[i - count_1] == 0:
        count_1 += 1
    elif lst_1[i - count_2] < 0:
        lst_1.append(lst_1[i - count_2])
        lst_1.remove(lst_1[i - count_2])
        count_2 += 1
while count_1:
    lst_1.append(0)
    count_1 -= 1
print(lst_1)

# 5
lst_1 = [5, 2, 7, 3, 8, 2, 4, 1, 6, 5]
lst_2 = lst_1.copy()
count_2 = 0
for i in range(len(lst_1)):
    count_1 = lst_1.count(lst_1[i])
    if count_1 == 1:
        count_2 += 1
        lst_2.insert(i + count_2, lst_1[i])
print(lst_2)

# 1
str_1 = input()
numbers = str_1.split(' ')
set_1 = set()
for number in numbers:
    if number not in set_1:
        set_1.add(number)
        print('NO')
    else:
        print('YES')

# 2
n = int(input())
set_1 = set(range(1, n + 1))
set_yes = set()
set_no = set()
while True:
    str_1 = input()
    str_1 = str_1.strip()
    lst_1 = str_1.split()
    len_1 = len(lst_1)
    if len_1 == 0:
        break
    elif lst_1[len_1 - 1] == "YES":
        for i in range(len_1 - 1):
            if int(lst_1[i]) <= n:
                lst_1[i] = int(lst_1[i])
                set_yes.add(lst_1[i])
        set_1 = set_yes - set_1
    elif lst_1[len_1 - 1] == "NO":
        for i in range(len_1 - 1):
            if int(lst_1[i]) <= n:
                lst_1[i] = int(lst_1[i])
                set_no.add(lst_1[i])
        set_1 -= set_no
print(set_1)
