
# Импортируем модуль datetime для работы со временем
from datetime import datetime

# Спрашиваем имя пользователя
name = input("Введите свое имя: ")

# Получаем текущую дату и время
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Выводим приветствие
print(f"\nПривет, {name}!")
print("Добро пожаловать в мир Termux и Python!")
print(f"Ваше первое приложение запущено: {current_time}")



