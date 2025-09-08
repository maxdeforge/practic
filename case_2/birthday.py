import datetime
import re
def main():
    print("Добро пожаловать! Пожалуйста, введите дату вашего рождения.")
    day = get_valid_input("Введите день (число от 1 до 31): ", 1, 31)
    month = get_valid_input("Введите месяц (число от 1 до 12): ", 1, 12)
    year = get_valid_input("Введите год (число от 1900 до текущего года): ", 1900, datetime.date.today().year)
    try:
        birth_date = datetime.date(year, month, day)
    except ValueError as e:
        print(f"Ошибка: {e}. Такая дата не существует.")
        return
    day_of_week = get_day_of_week(birth_date)
    print(f"Вы родились в {day_of_week}.")
    leap_status = "високосный" if is_leap_year(year) else "не високосный"
    print(f"{year} год был {leap_status}.")
    age = calculate_age(birth_date)
    print(f"Вам сейчас {age}.")
    print("\nВаша дата рождения на электронном табло:")
    print_digital_date(day, month, year)
def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Пожалуйста, введите число от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")
def get_day_of_week(date):
    days_rus = ["Понедельник", "Вторник", "Среда", "Четверг", 
                "Пятница", "Суббота", "Воскресенье"]
    return days_rus[date.weekday()]
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
def print_digital_date(day, month, year):
    day_str = str(day).zfill(2)
    month_str = str(month).zfill(2)
    year_str = str(year).zfill(4)
    date_string = f"{day_str} {month_str} {year_str}"
    digit_patterns = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': ['  *', '  *', '  *', '  *', '  *'],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', '***', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['***', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '***'],
        ' ': ['   ', '   ', '   ', '   ', '   ']
    }
    output_lines = ['', '', '', '', '']
    for char in date_string:
        pattern = digit_patterns.get(char, digit_patterns[' '])
        for i in range(5):
            output_lines[i] += pattern[i] + ' '
    for line in output_lines:
        print(line)

if __name__ == "__main__":
    main()
input("\nНажмите Enter для выхода...")