# task_1
i = 10
print (i)
j = "Привет!"
print (j)
var = input('Введите любое число:')
print('Вы ввели число', var)

#task_2
ss = int(input('Введите количество секунд'))
hours = ss / 3600
minutes = ss / 60
print(f"Время в формате чч:мм:сс составляет: {hours} :{minutes}: {ss}")

# task_3
n = '3'
n_n = n + n
print (n_n)
n_n_n = n + n + n
print (n_n_n)
sum = int(n) + int(n_n) + int(n_n_n)
print (sum)

# task_3
numeral = 1238587
max = numeral % 10
while numeral > 0:
    numeral = numeral // 10
    if numeral % 10 > max:
        max = numeral % 10
    if numeral > 9:
        continue
    else:
        print ('Наибольшее число:', max)

# task_4
revenue = input ('Введите значение выручки')
costs = input ('Введите сумму издержек')
profit = int(revenue) - int(costs)
if profit > 0:
    profitability = profit / int(revenue) * 100
    print ('Прибыль равна:', profit)
    print ('Рентабельность составляет', profitability, '%')
else:
    print ('Убыток составляет:', profit)
number_of_employees = input ('Введите количество сотрудников')
if profit > 0:
    profitab_of_emp = profit / int(number_of_employees) * 100
    print ('Прибыль на одного работника составляет', profitab_of_emp, '%')
else:
    print('В Вашей фирме убыток')

#task_6
a = int(input('Введите Ваш результат в первый день (в км)'))
b = int(input('Введите Вашу цель (в км)'))
day = 1
km = a
while km < b:
    a = a * 1.1
    day = day + 1
    km = km + a
print(f"Вы достигнете целевого результата в {km} км, на {day} день")


