
import random
import string

# 1. Определяем набор символов
# string.ascii_letters: A-Z, a-z
# string.digits: 0-9
# string.punctuation: специальные символы (!@#$%^...)
characters = string.ascii_letters + string.digits + string.punctuation

# 2. Получаем желаемую длину пароля
while True:
        try:
                    length = int(input("Введите желаемую длину пароля (например, 12): "))
                            if length > 0:
                                            break
                                                else:
                                                                print("Длина должна быть положительным числом.")
                                                                    except ValueError:
                                                                                print("Пожалуйста, введите корректное число.")


                                                                                # 3. Генерируем пароль с помощью цикла 'for'
                                                                                # В Python цикл 'for' часто используется для повторения действия
                                                                                # определенное количество раз.
                                                                                password = ""
                                                                                for i in range(length):
                                                                                        # Выбираем случайный символ из нашего набора и добавляем его к паролю
                                                                                            random_char = random.choice(characters)
                                                                                                password += random_char

                                                                                                # 4. Выводим результат
                                                                                                print(f"\nВаш сгенерированный пароль: {password}")
                                                                                                print(f"Длина: {length}")

