import re
from typing import Callable

#Створюємо функцію для знаходження всіх дійсних чисел з тексту
def generator_numbers(text: str):
    if text is not None:
        patern = r'[-+]?\d*\.\d+|\d+' #регулярний вираз для пошуку дійсних чисел
        matches = re.findall(patern, text)
    #Ітеруємося по знайденим числам 
        for match in matches:
            yield float(match) #використовуємо yield для створення генератора
    
    
def sum_profit(r, func: Callable):
    #використовуємо генератор для обчислення загальної суми чисел
    numbers_generator = func(text)
    #Підсумовуємо всі числа
    total_sum = sum(numbers_generator)
    return total_sum

#Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,\
    доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")