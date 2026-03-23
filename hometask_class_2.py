# 1
from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):

    def __init__(self, card_number: int):
        self.card_number = card_number

    def pay(self, amount):
        return f"Оплачено {amount} руб. кредитной картой **** **** **** {str(self.card_number)[-4:]}"

class Cash(PaymentMethod):

    def pay(self, amount):
        return f"Оплачено {amount} руб. наличными"


class Phone(PaymentMethod):

    def __init__(self, phone):
        self.phone = phone

    def pay(self, amount):
        return f"Оплачено {amount} руб. по № телефону ***-**-***-{str(self.phone)[-4:-2]}-{str(self.phone)[-2:]}"


pay_1 = CreditCard(123456789123456)
pay_2 = Cash()
pay_3 = Phone(375293332299)

payments = [pay_1, pay_2, pay_3]
for payment in payments:
    print(payment.pay(100))

# 2
from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class Telegram(Notification):

    def send(self, message):
        return f"{message}, добро пожаловать в telegram"

class Vkontakte(Notification):

    def send(self, message):
        return f"{message}, добро пожаловать во вконтакте"


class Mail(Notification):

    def send(self, message):
        return f"{message}, добро пожаловать в mail.ru"


message_1 = Telegram()
message_2 = Vkontakte()
message_3 = Mail()

massages = [message_1, message_2, message_3]
for message in massages:
    print(message.send('Привет!'))

# 3
class User:
    ROLES = ['admin', 'moderator', 'user', 'guest']

    def __init__(self, role):
        if role in self.ROLES:
            self.role = role


class PolicyAccess():

    def can_view(self, user):
        return user.role != 'guest'

    def can_edit(self, user):
        return user.role in ['admin', 'moderator']

    def can_delete(self, user):
        return user.role == 'admin'

def check_policy(cls, method):
    def decorator(func):
        def wrapper(user):
            policy = cls()
            policy_method = getattr(policy, method)
            if policy_method(user):
                return func()
            else:
                return "Доступ запрещен"
        return wrapper
    return decorator

@check_policy(PolicyAccess, 'can_view')
def view_document():
    return "Просмотр документа разрешён"

@check_policy(PolicyAccess, 'can_edit')
def edit_document():
    return "Изменение документа разрешено"

@check_policy(PolicyAccess, 'can_delete')
def delete_document():
    return "Удаление документа разрешено"


user_1 = User('admin')
user_2 = User('moderator')
user_3 = User('guest')
user_4 = User('user')

print(edit_document(user_1))
print(edit_document(user_4))
print(view_document(user_3))
print(view_document(user_4))


# 4
from datetime import date

class BankAccount:
    TODAY = date.today()

    def __init__(self, balance: float = 0):
        self.__balance = balance
        self.daily_limit = 5000
        self.withdrawals_today = 0
        self.max_withdrawals = 3
        self.withdraw_money_today = 0

    def deposit(self, amount: float):
        self.__balance += amount

    def withdraw(self, amount: float):
        if self.TODAY != date.today():
            self.withdraw_money_today = 0
            self.withdrawals_today = 0
        if amount > self.__balance:
            return "Недостаточно средств!"
        elif self.withdrawals_today == self.max_withdrawals:
            return "Достигнут лимит операций!"
        elif self.withdraw_money_today + amount > self.daily_limit:
            return "Снятие средств сверх дневного лимита невозможно!"
        else:
            self.__balance -= amount
            self.withdrawals_today += 1
            return f"Произошло снятие {amount} рублей. это {self.withdrawals_today}-ая операция за день"

    def get_balance(self):
        return self.__balance
