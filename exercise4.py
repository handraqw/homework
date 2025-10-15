from random import choice, randint, shuffle
from string import ascii_uppercase, ascii_lowercase

"""
Функции, которые выводят рандомный символ
"""
def random_up_letter():
    return choice(ascii_uppercase)

def random_low_letter():
    return choice(ascii_lowercase)

def random_digit():
    return str(randint(0,9))

def random_symbol():
    special_symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@',
    '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~']
    return choice(special_symbols)


"""
Консольный интерфейс с вопросами о характеристиках пароля
"""
print("Генератор паролей!\n\n")

lowercase_status = int(input("Использовать нижный регистр? \n1 - Да, 0 - Нет.\n"))
uppercase_status = int(input("Использовать верхний регистр? \n1 - Да, 0 - Нет.\n"))
special_symbols_status = int(input("Использовать специальные символы? \n1 - Да, 0 - Нет.\n"))
digits_status = int(input("Использовать цифры? \n1 - Да, 0 - Нет.\n"))
password_length = int(input("Введите длину пароля:\n"))


"""
Генерация пароля
"""
password = ""

while len(password) < password_length:
    if special_symbols_status == 1:
        password += random_symbol()
    if digits_status == 1:
        password += random_digit()
    if lowercase_status == 1:
        password += random_low_letter()
    if uppercase_status == 1:
        password += random_up_letter()

while len(password) != password_length:
    password = password[:-1]

"""
Шаффл пароля
"""    
password_list = list(password)
shuffle(password_list)
shuffled_password = ''.join(password_list)

print(shuffled_password)
