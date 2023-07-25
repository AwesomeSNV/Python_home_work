from random import randint

# Список друзей пошедших в поход
friend_names = []
friend_names.append("Иван")
friend_names.append("Федор")
friend_names.append("Николай")

# Список вещей
thing = []
thing.append("Палатка")
thing.append("Рюкзак")
thing.append("Спальный мешок")
thing.append("Спички")
thing.append("Топор")
thing.append("Вода")
thing.append("Провиант")

group = {}

for friend in friend_names:
    thing_quantity = randint(0, len(thing)-1)
    thing_taken = []

    while thing_quantity != 0:
        j = randint(0, len(thing)-1)
        if thing[j] in thing_taken:
            pass
        else:
            thing_taken.append(thing[j])
            thing_quantity -= 1
    group[friend] = thing_taken

print(group)

all_thing = set()
for name in friend_names:
    all_thing = all_thing.union(group.get(name))

print(all_thing)

for current_thing in all_thing:
    count = 0
    for name in friend_names:
        if current_thing in group.get(name):
            count += 1

    if count == len(friend_names):
        print (f"{current_thing} - есть у каджого.")

    elif count == len(friend_names)-1:
        for name in friend_names:
            if current_thing not in group.get(name):
                print(f"{name} не взял с собой {current_thing}.")
                break

    elif count == 1:
        for name in friend_names:
            if current_thing in group.get(name):
                print(f"{name} единственный кто взял {current_thing}.")
                break