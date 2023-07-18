from random import randint

Low_limit = 0
Up_limit = 1000

number = randint(Low_limit, Up_limit)

count = 10

while count > 0:
    user_number = int(input("Введите целое число  У вас {} попыток: ".format(count)))
    if number > user_number:
        print("Загаданое число больше чем ", user_number)
    elif number < user_number:
        print("Загаданое число меньше чем ", user_number)
    else:
        print("Угадали")
        quit()
    count -= 1

print("Попытки исчерпаны")