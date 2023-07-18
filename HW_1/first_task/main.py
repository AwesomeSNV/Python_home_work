def input_parametr(str_parametr):
    while True:
        parametr = input("Введите длину стороны  {} : ".format(str_parametr))
        try:
            parametr = float(parametr)
        except:
            print("{} должно быть числом".format(str_parametr))
        else:
            if parametr > 0:
                return parametr
            else:
                print("{} должно быть положительным числом".format(str_parametr))

print("Введите стороны треугольника а, b, c")

side_a = input_parametr("а")
side_b = input_parametr("b")
side_c = input_parametr("c")

if side_a >= side_b+side_c or side_b >= side_a+side_c or side_c >= side_b+side_a:
    print("Заданный треугольник существовать не может")

else:
    print("Заданный треугольник существует")
    if side_a == side_b == side_c:
        print("Заданный треугольник равносторонний")
    elif side_a == side_b or side_a == side_c or side_c == side_b:
        print("Заданный треугольник равнобедренный")