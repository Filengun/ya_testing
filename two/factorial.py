print('Привет, Никита. Введи число для подсчета факториала')
number = int(input())

if number <= 4:
    print('Попробуй ввести число больше')
else:
    fact = 1
    for i in range(5, number+1):
        fact = fact * i
    print(f"факториал равен - {fact}")