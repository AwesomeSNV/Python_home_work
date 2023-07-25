enter_string = input("Введите строку: ").lower()
simbols = "+-—.,;:!?,'"""
num_of_often_words = 10

for char in simbols:
    user_string = user_string.replace(char, " ")

word_list = user_string.split(" ")

empty_char = word_list.count("")

for i in range(empty_char):
    word_list.remove("")

all_words_set = set(word_list)

word_dict = {}

for word in all_words_set:
    word_dict[word] = word_list.count(word)

for i in range (num_of_often_words):
    max_count = 0
    current_key = ""
    for word in all_words_set:

        if word_dict.get(word) > max_count:
            max_count = word_dict.get(word)
            current_key = word
    print(f"{i+1} место среди самых часто встречающихся слов занимает {current_key}. Появляется в тексте {word_dict.get(current_key)} колличество раз.")
    del word_dict[current_key]
    all_words_set.remove(current_key)