"""
2023/11/30 00:00|Домашнее задание по теме "Генераторы"
Цель работы
Более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
Задание
Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки. В функцию передаётся только сама строка.
Примечание
Используйте оператор yield
Входные данные
a = all_variants("abc")
for i in a:
 print(i)
Выходные данные
a
b
c
ab
bc
abc
Часто задаваемые вопросы:
один из вариантов функции генерирующей все последовательные подстроки
def all_variants(text):
for start in range(len(text)):
for end in range(start+1, len(text)+1):
yield text[start:end]
for substr in all_variants('12345'):
print(substr)
https://onlinegdb.com/o2YO_PBKs
"""
