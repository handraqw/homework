from random import choice, randint, shuffle
from string import ascii_uppercase, ascii_lowercase

"""
Функции, которые возвращают случайный символ:
- random_up_letter() — случайная заглавная буква A-Z
- random_low_letter() — случайная строчная буква a-z
- random_digit() — случайная цифра 0-9 в виде строки
- random_symbol() — случайный специальный символ с клавиатуры
"""
def random_up_letter():
    return choice(ascii_uppercase)

def random_low_letter():
    return choice(ascii_lowercase)

def random_digit():
    return str(randint(0,9))  # преобразуем в строку, чтобы можно было складывать с паролем

def random_symbol():
    special_symbols = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
        ':', ';', '<', '=', '>', '?', '@',
        '[', '\\', ']', '^', '_', '`',
        '{', '|', '}', '~'
    ]
    return choice(special_symbols)


"""
Консольный интерфейс — спрашиваем у пользователя характеристики пароля
"""
print("Генератор паролей!\n\n")

lowercase_status = int(input("Использовать нижний регистр? \n1 - Да, 0 - Нет.\n"))
uppercase_status = int(input("Использовать верхний регистр? \n1 - Да, 0 - Нет.\n"))
special_symbols_status = int(input("Использовать специальные символы? \n1 - Да, 0 - Нет.\n"))
digits_status = int(input("Использовать цифры? \n1 - Да, 0 - Нет.\n"))
password_length = int(input("Введите длину пароля:\n"))


"""
Генерация пароля:
- Пока длина пароля меньше нужной, добавляем случайные символы
- Добавляем символы в зависимости от выбранных опций пользователя
- В конце может получиться длиннее, чем нужно, поэтому обрезаем лишние символы
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

# Если случайно получилось больше нужной длины, обрезаем лишние символы
while len(password) != password_length:
    password = password[:-1]

"""
Шаффл пароля:
- Перемешиваем символы в случайном порядке, чтобы типы символов были распределены случайно
"""
password_list = list(password)  # превращаем строку в список символов
shuffle(password_list)          # перемешиваем список
shuffled_password = ''.join(password_list)  # собираем обратно в строку

# Выводим готовый пароль
print(shuffled_password)
