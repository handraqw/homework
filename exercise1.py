def transform(letter, step):
    """
    Функция для шифра Цезаря.
    
    Args:
        letter (str): одиночный символ
        step (int): шаг сдвига для шифрования (может быть отрицательным для расшифровки)
    
    Returns:
        str: новый символ после сдвига. 
             Если символ не является буквой, возвращается без изменений.
    """
    letter_code = ord(letter)

    # Английский алфавит — строчные буквы (a-z)
    if 97 <= letter_code <= 122: 
        step %= 26
        if letter_code + step <= 122:
            return chr(letter_code + step)
        else: 
            return chr(letter_code + step - 122 + 96)

    # Английский алфавит — заглавные буквы (A-Z)
    if 65 <= letter_code <= 90: 
        step %= 26
        if letter_code + step <= 90:
            return chr(letter_code + step)
        else: 
            return chr(letter_code + step - 90 + 64)
    
    # Русский алфавит — строчные буквы (а-я)
    if 1072 <= letter_code <= 1103: 
        step %= 32
        if letter_code + step <= 1103:
            return chr(letter_code + step)
        else: 
            return chr(letter_code + step - 1103 + 1071)
        
    # Русский алфавит — заглавные буквы (А-Я)
    if 1040 <= letter_code <= 1071: 
        step %= 32
        if letter_code + step <= 1071:
            return chr(letter_code + step)
        else: 
            return chr(letter_code + step - 1071 + 1039)
    
    # Все остальные символы (цифры, спецсимволы) остаются без изменений
    return letter


def lang_detect(letter):
    """
    Определяет язык текста по первому символу
    
    Args:
        letter (str): символ для проверки
    
    Выводит на экран сообщение о языке:
        - Английский
        - Русский
    """
    letter_code = ord(letter)
    if 97 <= letter_code <= 122 or 65 <= letter_code <= 90:
        print("\nТекст на английском\n")
    if 1072 <= letter_code <= 1103 or 1040 <= letter_code <= 1071:
        print("\nТекст на русском\n")


"""
Главная часть программы
"""
print("Это шифратор Цезаря!")
print("Если вы хотите зашифровать осмысленный текст напишите 1")
print("Если вы хотите расшифровать текст напишите 2")
mode_selector = int(input())

print("Введите текст:")
text_from_user = input()

# Определяем язык по второму символу (можно менять на первый)
lang_detect(text_from_user[1])

print("Введите шаг:")
cipher_step = int(input())

# Если выбрали расшифровку, делаем шаг отрицательным
if mode_selector == 2:
    cipher_step = -1 * cipher_step

# Применяем функцию transform() ко всем символам строки
new_text = ""
for char in text_from_user:
    new_text += transform(char, cipher_step)

# Выводим зашифрованный или расшифрованный текст
print(new_text)
