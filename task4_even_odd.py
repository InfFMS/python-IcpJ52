# Задача 4: Проверка на четность
# Напишите программу, которая запрашивает у пользователя число и определяет, является ли оно четным или нечетным.
# Пример:
# Ввод: 8
# Вывод: Число 8 четное
num = int(input("Введите число: "))
if num % 2 == 0:
    print(f'Число {num} четное')
else:
    print(f'Число {num} нечетное')
