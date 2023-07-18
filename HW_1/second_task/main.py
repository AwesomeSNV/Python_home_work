number = None
flag = False

while not flag:
    number = input("Введите положительное целое число от 2 до 100000: ")
    flag = number.isdigit()
    if flag:
        if 1 < int(number) < 100000:
            pass
        else:
            flag = False

number = int(number)

for i in range (2, int(number/2)+1):
    if number % i == 0:
        print("Введенное число {} не является простым".format(number))
        quit()

print("Введенное число {} является простым".format(number))