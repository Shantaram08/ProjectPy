# Задание №1
print('Hello world')
user = input('I am Python. What is your name : ?')
print('Welcome', user)
fn = int(input('Введите первое число :  '))
sn = int(input('Введите второе число : '))
print(fn + sn)
# Задание №2
sec = int(input("Введите количество секунд : "))
h = sec // 3600
m = (sec - h * 3600) // 60
s = sec % 60
print(h, 'час', m, 'мин', s, 'сек')
# Задание №3
number = int(input("Введите число : "))
tem = str(number)
v1 = tem + tem
v2 = tem + tem + tem
var = number + int(v1) + int(v2)
print("Результат:", var)
# Задание №4
i = int(input('Введите число : '))
ls = []
while i > 10:
    ls.append(i % 10)
    i //= 10
max_number = max(ls)
print('Самая большая цифра в числе : ', max_number)
# Задание №5
proceeds = float(input('Введите значение выручки :'))
costs = float(input('Введите значение издержек : '))
if proceeds > costs:
    print('Фирма работает в прибыль')
    profit = proceeds - costs
    profitability = profit / proceeds
    print(f' коэффициент рентабельности равен {profitability}')
    number_of_employees = int(input('Введи количество сотрудников : '))
    print(f'Прибыль фирмы на одного сотрудника равняется {round(profit / number_of_employees, 2)}y.e.')
elif proceeds < costs:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')
# Задание №6
a = int(input('Введите результат первого дня : '))
b = float(input('Желаемый результат : '  ))
day = 1
while a < b:
    a *= 1.1
    day += 1
print('Результат будет достигнут на ', day, 'день.')
