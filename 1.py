#Вариант 4 Реализовать функцию, которая будет проверять, является ли введенная строка датой в формате DD/MM/YYYY, возвращаемое значение true или False.
#Дополнительно реализовать функцию, которая выбрасывает исключение о некорректном аргументе, иначе возвращает дату в формате DD/MM/YYYY.

import re

def is_valid_date(date_str):
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    return bool(re.match(pattern, date_str))

def validate_date(date_str):
    if not is_valid_date(date_str):
        raise ValueError("Некорректный формат даты. Дата должна быть в формате DD/MM/YYYY.")
    
    day, month, year = map(int, date_str.split('/'))
    
    if day < 1 or day > 31:
        raise ValueError("Некорректный день.")
    if month < 1 or month > 12:
        raise ValueError("Некорректный месяц.")
    if year < 1000 or year > 9999:
        raise ValueError("Некорректный год.")
    
    return date_str

def main():
    user_input = input("Введите дату в формате DD/MM/YYYY: ")
    try:
        validated_date = validate_date(user_input)
        print(f"Введенная дата {validated_date} является корректной.")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
