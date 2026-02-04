# 1
class TwoVar(object):
    def __init__(self, var_1 = 5, var_2 = 16) -> None:
        self.var_1 = var_1
        self.var_2 = var_2

    def view(self) -> None:
        print(f"{self.var_1}\n{self.var_2}")

    def set_var(self, var_1 : int, var_2 : int) -> None:
        self.var_1 = var_1
        self.var_2 = var_2

    def sum(self) -> int:
        return self.var_1 + self.var_2

    def maximum(self) -> int:
        return self.var_1 if self.var_1 > self.var_2 else self.var_2


two_var = TwoVar()
two_var.view()
two_var.set_var(var_1=6, var_2=3)
print(two_var.sum())
print(two_var.maximum())

# 2
class TenCounter(object):
    def __init__(self, count):
        self.count = count
        self.start = 0
        self.end = 9

    @property
    def current_value(self):
        return self.count

    def set_range(self, start : int, end : int):
        self.start = start
        self.end = end

    def plus_one(self):
        if self.count == self.end:
            self.count = self.start
        else:
            self.count += 1
        return self.count

    def minus_one(self):
        if self.count == self.start:
            self.count = self.end
        else:
            self.count -= 1
        return self.count


counter = TenCounter(7)
print(counter.current_value)
counter.plus_one()
print(counter.current_value)
counter.plus_one()
print(counter.current_value)
counter.minus_one()
print(counter.current_value)

sign = input('Введите "plus" или "minus"')
num_1 = int(input('Введите число операций'))
if sign == 'plus':
    for _ in range(num_1):
        counter.plus_one()
elif sign == 'minus':
    for _ in range(num_1):
        counter.minus_one()
else:
    print('Вы ввели не корректные данные')

print(counter.current_value)

# 3
class Shop(object):

    def __init__(self):
        self.product = set()

    def get_product(self):
        return self.product

    def find_product(self, product):
        if product in self.product:
            return f"{product} имеется в магазине"
        else:
            return f"{product} нет в наличии"

    def add_product(self, product):
        self.product.add(product)

    def del_product(self, product):
        if product in self.product:
            self.product.remove(product)

shop = Shop()
shop.add_product('Гречка')
shop.add_product('Молоко')
shop.add_product('Яблоко')
shop.add_product('Хлеб')
print(shop.get_product())
print(shop.find_product("Гречка"))
print(shop.find_product("Сахар"))
shop.add_product('Яйца')
shop.del_product('Яблоко')
shop.del_product('Мука')
print(shop.get_product())

# 4
class MoneyBox(object):
    CAPACITY = 60
    COINS = 0

    def __init__(self, money: int = COINS, amount : int = CAPACITY) -> None:
        self.money = money
        self.amount = amount

    def info(self):
        print(f"Копилка заполнена на {self.money} из {self.amount}, в копилку можно добавить еще {self.amount - self.money}")

    def can_add(self, v):
        return (self.money + v) <= self.amount

    def add(self, v):
        self.money += v

money_box = MoneyBox(amount=100)
money_box.info()
if money_box.can_add(30):
    money_box.add(30)
money_box.info()
if money_box.can_add(30):
    money_box.add(30)
money_box.info()
if money_box.can_add(30):
    money_box.add(30)
money_box.info()
if money_box.can_add(30):
    money_box.add(30)
money_box.info()