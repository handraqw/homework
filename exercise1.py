def transform(letter, step):
    letter_code = ord(letter)

    # Английский + нижний регистр
    if 97 <= letter_code <= 122: 
        step %= 26 # если шаг больше одного оборота 
        if letter_code + step <= 122:
            return chr(letter_code + step)
        else: 
            return chr(letter_code + step - 122 + 96)

    # Английский + верхний регистр
    if 65 <= letter_code <= 90: 
        step %= 26 # если шаг больше одного оборота 
        if letter_code + step <= 90:
            return chr(letter_code + step)
        else: 
            return chr(letter_code + step - 90 + 64)
    
    # Русский + нижний регистр
    if 1072 <= letter_code <= 1103: 
        step %= 32 # если шаг больше одного оборота 
        if letter_code + step <= 1103:
            return chr(letter_code + step)
        else: 
            return chr(letter_code + step - 1103 + 1071)
        
    # Русский + верхний регистр
    if 1040 <= letter_code <= 1071: 
        step %= 32 # если шаг больше одного оборота 
        if letter_code + step <= 1071:
            return chr(letter_code + step)
        else: 
            return chr(letter_code + step - 1071 + 1039)
    
    # Если символ не является буквой, то он остается прежним
    return letter

def lang_detect(letter):
    letter_code = ord(letter)
    if 97 <= letter_code <= 122 or 65 <= letter_code <= 90:
        print("\nТекст на английском\n")
    if 1072 <= letter_code <= 1103 or 1040 <= letter_code <= 1071:
        print("\nТекст на русском\n")


"""
Шифр Цезаря

Функция transform() принимает на вход букву, далее она определяет к какому языку относится буква.
Затем она возвращает новую букву с учетом шага.

Далее программа узнает какую функцию необходимо применить, шифрование или дешифрование и шаг
программа выведет язык текста и после вернет новую строчку

"""

print("Это шифратор Цезрая! \nЕсли вы хотите зашифровать осмысленный текст напишите 1\nЕсли вы хотите расшифровать текст напишите 2")
mode_selector = int(input())

print("Введите текст:")
text_from_user = input()

lang_detect(text_from_user[1])


print("Введите шаг:")
cipher_step = int(input())
if mode_selector ==  2:
    cipher_step = -1 * cipher_step


new_text = ""
for char in text_from_user:
    new_text += transform(char, cipher_step)

print(new_text)