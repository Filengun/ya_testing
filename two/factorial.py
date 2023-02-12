print('Привет, Никита. Введи число для подсчета суммы факториалов')
number = int(input())

if number <= 4:
    print('Попробуй ввести число больше')
else:
    fact = 1
    score = 0
    for i in range(5, number+1):
        fact = fact * i
        score +=fact
    print(f"Сумма факториалов равена - {score}")