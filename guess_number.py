from random import randint


hidden_number = randint(1, 100)
print('Угдайте число от 1 до 100')
    

while True:
    guess = int(input('Введите число: '))
    
    if hidden_number > guess:
        print('Ваше число меньше того, что загадано')
    
    elif hidden_number < guess:
        print('Ваше число больше того, что загадано')
    
    elif hidden_number == guess:
        break    
print('Отличная интуиция! Вы угадали число :)')
