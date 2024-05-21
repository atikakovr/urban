"""
2023/09/21 00:00|Практическое задание по уроку "Строки и индексация строк"
Зачёт
"""
my_string = 'Какое-то значение строки'
print('Первый: ', my_string[0])
print('Последний: ', my_string[-1])
print('Подстрока с третьего по пятый символы: ', my_string[2:6])
print('Cтрока наоборот: ', my_string[::-1])
print('String length: ', len(my_string))
my_str_1 = 'это новая строка'
my_str_2 = 'это моя строка'
my_str = my_str_1 + ' ' + my_str_2
print(my_str)