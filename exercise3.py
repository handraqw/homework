'''
Задание 3
'''
def print_pack_report(cake_count):
    """
    Определяет, как расфасовать пирожные.

    Проверяет количество пирожных и возвращает сообщение о способе их упаковки.

    Args:
        cake_count (int): Количество пирожных
    
    Returns:
        str: Сообщение о фасовке
            f"{temp_cake_count} - расфасуем по 3 или по 5"
            f"{temp_cake_count} - расфасуем по 3"
            f"{temp_cake_count} - расфасуем по 5"
            f"{temp_cake_count} - не заказываем!"
            "У вас нет пирожных"
    """

    for temp_cake_count in range(cake_count, 0, -1):
        if temp_cake_count % 3 == 0 and temp_cake_count % 5 == 0:
            print(f"{temp_cake_count} - расфасуем по 3 или по 5")
        elif temp_cake_count % 3 == 0:
            print(f"{temp_cake_count} - расфасуем по 3")
        elif temp_cake_count % 5 == 0:
            print(f"{temp_cake_count} - расфасуем по 5")
        else:
            print(f"{temp_cake_count} - не заказываем!")
