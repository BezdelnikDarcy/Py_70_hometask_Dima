# 1
try:
    x = (1, 2, 5, 7)
    x = x / 2
    print(x)
except TypeError:
    print("TypeError: unsupported operand type(s) for /: 'tuple' and 'int'")

# 2
try:
    str_1 = "abcdef"
    print(str_1[15])
except IndexError:
    print("IndexError: index out of range")

# 3
a = int(input())
b = int(input())
c = int(input())
try:
    if a == 0  or b == 0 or c == 0:
        raise ArithmeticError
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
except ArithmeticError:
    print("ArithmeticError")

# 4
lst_1 = [5, 2, 0, -2, -7, 1, 8, 0, -1]
try:
    lst_1.pop(20)
except IndexError:
    print("TypeError")

# 5
dict_1 = {"Name": "Dima", "Age": 26, "height": 180}
try:
    key_1 = input()
    print(dict_1[key_1])
except KeyError:
    print("KeyError")

# 6
str_1 = input()
lst_1 = str_1.split()
count_1 = 0
for i in range(len(lst_1)):
    try:
        count_1 += int(lst_1[i])
    except:
        count_1 = count_1
print(count_1)

# 7
str_1 = input()
str_1 = str_1.replace(' ', '')
try:
    if str_1.isdigit():
        raise TypeError
    else:
        dict_1 = {}
        lst_1 = []
        for i in str_1:
            if i not in dict_1:
                dict_1[i] = 0
                lst_1.append(i)
            dict_1[i] += 1
        for i in lst_1:
            print(i, dict_1[i])
except TypeError:
    print('TypeError')