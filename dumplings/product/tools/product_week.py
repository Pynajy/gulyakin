from datetime import datetime

def week_number_in_month(date_string):
    date_object = datetime.strptime(date_string, "%d-%m-%Y")
    
    # Определение первого дня месяца
    first_day_of_month = datetime(date_object.year, date_object.month, 1)
    
    # Вычисление разницы в днях
    delta = date_object - first_day_of_month
    
    # Определение номера недели в месяце
    week_number = delta.days // 7 + 1
    
    return week_number

# Пример использования
# today = datetime.now()
# result = week_number_in_month(today)
# print(f"The week number for {today.strftime('%Y-%m-%d')} is {result}")
