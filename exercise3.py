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
            f"{cake_count} - расфасуем по 3 или по 5"
            f"{cake_count} - расфасуем по 3"
            f"{cake_count} - расфасуем по 5"
            f"{cake_count} - не заказываем!"
            "У вас нет пирожных"
    """
    if  cake_count > 1:
        if cake_count % 3 == 0 and cake_count % 5 == 0:
            return f"{cake_count} - расфасуем по 3 или по 5"
        elif cake_count % 3 == 0:
            return f"{cake_count} - расфасуем по 3"
        elif cake_count % 5 == 0:
            return f"{cake_count} - расфасуем по 5"
        else: return f"{cake_count} - не заказываем!"
    else:
        return "У вас нет пирожных"


