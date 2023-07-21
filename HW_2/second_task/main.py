from fractions import Fraction

def gcd_user(a,b):
    while b != 0:
        a, b = b, a % b
    return a

print("Cложение и умножение натуральных дробей:")
numerator_1, denominator_1 = input("Введите первую натуральную дробь a/b: ").split("/")
numerator_2, denominator_2 = input("Введите вторую натуральную дробь a/b: ").split("/")

numerator_1 = int(numerator_1)
denominator_1 = int(denominator_1)
numerator_2 = int(numerator_2)
denominator_2 = int(denominator_2)

# Cложение дробей
summ_numerators = numerator_1 * denominator_2 + numerator_2 * denominator_1
summ_denominators = denominator_2 * denominator_1

res_summ_numumerators = int(summ_numerators / gcd_user(summ_numerators, summ_denominators))
res_summ_denominators = int(summ_denominators / gcd_user(summ_numerators, summ_denominators))

print(f"Сумма двух дробей = : {res_summ_numumerators}/{res_summ_denominators}")
print("Проверка через Fractions: ", Fraction(numerator_1, denominator_1)+Fraction(numerator_2, denominator_2))

# Умножение дробей
mult_numerators = numerator_1 * numerator_2
mult_denominators = denominator_2 * denominator_1

res_mult_num = int(mult_numerators / gcd_user(mult_numerators, mult_denominators))
res_mult_denom = int(mult_denominators / gcd_user(mult_numerators, mult_denominators))

print(f"Произведение двух дробей = : {res_mult_num}/{res_mult_denom}")
print("Произведение через Fractions: ", Fraction(numerator_1, denominator_1)*Fraction(numerator_2, denominator_2))