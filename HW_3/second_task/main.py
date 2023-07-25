current_list = [1, 2, 1, 2, 3, 5, 3, 4, 5, 6, 3]
i = 0
new_list = []
while i < len(current_list):
    if current_list.count(current_list[i]) > 1:
        temp = current_list[i]
        for j in range(current_list.count(temp)):
            current_list.remove(temp)
        new_list.append(temp)
    else:
        i += 1
print(current_list)
print(new_list)