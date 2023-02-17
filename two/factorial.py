import math

print('Привет, как тебя зовут?')
first_name = str(input())
print(f'{first_name.title()}, веди число больше 5 для подсчета суммы факториалов.')
number = int(input())
sum_fact = 0
if number < 5:
    print('Необходимо число больше 5')
else:
    for i in range(5, number+1):
        fact = math.factorial(i)
        sum_fact +=fact
    print(f'Сумма факториалов {sum_fact}')

