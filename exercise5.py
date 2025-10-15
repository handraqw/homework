def rome_converter(roman_number):
    """
    Конвертирует римское число в арабское.

    Args:
    roman_number (str): Римское число в виде строки, например "XIV".

    Returns:
    int: Арабское число, соответствующее римскому числу.
    """

    roman_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 

    arab_num = 0
    previous_num = 0

    for digit in reversed(roman_number):
        current_num = roman_digits[digit]
        if current_num < previous_num:
            arab_num -= current_num
        else:
            arab_num += current_num
        previous_num = current_num
    return arab_num
    
