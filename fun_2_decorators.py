# 1
def log_result(fun):
    def inner(n: int):
        result = fun(n)
        print(result)
        return result
    return inner

def square(n: int):
    return n ** 2

decorator_result = log_result(square)

n = int(input())

decorator_result(n)

# 2
def some_fun():
    print('Hello world!')

def repeat(n: int):
    def inner(fun):
        def wrapper():
            for i in range(n):
                fun()
        return wrapper
    return inner

n = int(input())
decorator_result = repeat(n)
decorator_repeat = decorator_result(some_fun)
decorator_repeat()

# 3
def bench(fun):
    def wrapper(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
    return wrapper

def some_fun(a,b):
    print(a / b)

some_fun = bench(some_fun)

num_1 = int(input())
num_2 = int(input())
some_fun(num_1,num_2)

# 4
def count_words(text):
    lst_nums = []
    for i in range(len(text)):
        lst_nums.append(len(text[i]))
    return lst_nums
lst_1 = input().split()
print(count_words(lst_1))

# 5
def lowwer_words(text):
    return [word for word in text if word.islower()]
lst_1 = ['apple', 'Banana', 'cherry', 'DATE']
print(lowwer_words(lst_1))

# 6
def comming_of_age(text):
    return [tup for tup in text if tup[1] > 18]
lst_1 = [('Дима', 26), ('Никита', 23), ('Настя', 20), ('Ваня', 27), ('Валера', 15), ('Полина', 13), ('Глеб', 10)]
print(comming_of_age(lst_1))

# 7
from functools import reduce

lst_1 = [[1,2],[3,4],[5,6]]
lst_2 = reduce(lambda x, y: x + y, lst_1)
print(lst_2)

# 8
lst_1 = ['cat','car','mouse','dog','snake','cow']
dict_1 = {}
for key in lst_1:
    if key[0] not in dict_1:
        dict_1[key[0]] = [key]
    else:
        dict_1[key[0]].append(key)
print(dict_1)

# 9
lst_1 = [('milk', 3, 5), ('burger', 8, 2), ('bread', 2, 10), ('juice', 4, 6)]
lst_2 = []
for product in lst_1:
    sum_1 = product[1] * product[2]
    lst_2.append(sum)
print(lst_2)