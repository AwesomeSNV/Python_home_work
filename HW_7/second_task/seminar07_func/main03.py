# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
import itertools

def multiply_files(names_file_path: str, numbers_file_path: str):
    names_size = len(list(1 for _ in open(names_file_path)))
    nums_size = len(list(1 for _ in open(numbers_file_path)))
    count = max(nums_size, names_size)
    with open('res.txt', 'w', encoding="utf-8") as res, \
            open(names_file_path, 'r', encoding="utf-8") as names, \
            open(numbers_file_path, 'r', encoding="utf-8") as example:
        names_str = itertools.cycle(names.readlines())
        example_str = itertools.cycle(example.readlines())

        for i in range(count):
            example_str1, example_str2 = next(example_str).split('|')
            prod = float(example_str1) * float(example_str2)
            if prod < 0:
                res.write(f'{next(names_str).strip().lower()} {abs(prod)}\n')
            else:
                res.write(f'{next(names_str).strip().upper()} {round(prod)}\n')

if __name__ == "__main__":
    multiply_files("names.txt", "numbers.txt")