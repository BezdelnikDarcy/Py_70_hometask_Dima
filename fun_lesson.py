# 1
a = int(input())
b = int(input())
def min_1(a, b):
    if a < b:
        return a
    else:
        return b
a = min_1(a, b)
b = int(input())
a = min_1(a, b)
b = int(input())
print(min_1(a, b))

# 2
num_1 = int(input())
def perfect_num(num_1):
    sum_del = 0
    for i in range(1, num_1):
        if num_1 % i == 0:
            sum_del += i
    return sum_del
if perfect_num(num_1) == num_1:
    print('YES')
else:
    print('NO')

# 3
n = int(input())
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        num_1 = 1
        num_2 = 1
        for i in range(2, n):
            num_3 = num_2
            num_2 += num_1
            num_1 = num_3
        return num_2
print(fib(n))

# 4
x = int(input())
def closest_mod_5(x):
    return x + (5 - x % 5) % 5
print(closest_mod_5(x))

# 5
def check_variable(name_var):
    if not name_var or "-" in name_var or " " in name_var or name_var[0].isdigit():
        print('Нельзя использовать')
    else:
        print('Можно использовать')
while True:
    name_var = input()
    if name_var == 'Поработали, и хватит':
        break
    else:
        check_variable(name_var)

# 6
def odd_muns():
    return [i for i in range(11, 100, 2)]
print(odd_muns())

# 7
def multiple3_5():
    return [i for i in range(100,1000) if i % 3 == 0 and i % 5 == 0]
print(multiple3_5())

# 8
def set_nums():
    lst_1 = [1, 2, 2, 3, 5, 6, 6, 6, 6, 6, 7, 7, 9, 23, 56, 56, 78]
    counter = 1
    for i in range(len(lst_1) - 1):
        if lst_1[i] != lst_1[i + 1]:
            counter += 1
        else:
            continue
    return counter
print(set_nums())

# 9
def sum_neigh():
    nums = input()
    lst_1 = nums.split(' ')
    for i in range(len(lst_1) - 1):
        sum_1 = int(lst_1[i- 1]) + int(lst_1[i + 1])
        print(sum_1, end=' ')
    print(int(lst_1[0]) + int(lst_1[-2]))
sum_neigh()