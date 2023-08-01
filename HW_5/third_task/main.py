def fib_num(num):
    num1, num2 = 1, 1
    print(num1, num2, end=" " )
    for i in range(num + 1):
        yield num1+num2
        num1, num2 = num2, num1+num2

print(*fib_num(40))