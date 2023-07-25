things = {}
things["Палатка"] = 5
things["Провиант"] = 3
things["Вода"] = 2
things["Спальный мешок"] = 3
things["Инструмент"] = 4

taken_things = []

max_weight = 10

weight_left = max_weight

for key in things:
    if weight_left - things.get(key) >= 0:
        taken_things.append(key)
        weight_left -= things.get(key)

if not taken_things:
    print ("В рюкзак ничего не поместилось")
else:
    print(f"В рюкзак влезло {taken_things}")