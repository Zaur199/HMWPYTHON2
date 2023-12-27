#3. Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

import fractions

fraction1 = input("Введите первую дробь (в виде a/b): ")
fraction2 = input("Введите вторую дробь (в виде a/b): ")

numerator1, denominator1 = map(int, fraction1.split('/'))
numerator2, denominator2 = map(int, fraction2.split('/'))

sum_fraction = fractions.Fraction(numerator1, denominator1) + fractions.Fraction(numerator2, denominator2)
print(f'Сумма дробей: {sum_fraction}')

product_fraction = fractions.Fraction(numerator1, denominator1) * fractions.Fraction(numerator2, denominator2)
print(f'Произведение дробей: {product_fraction}')