def dictionary(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, str | int | float | bool | tuple):
            result[value] = key
        else:
            result[str(value)] = key
    return result

print(dictionary(string='STRING',
                     nunber=10,
                     logic=False,
                     user_list=['aaa', 'bbb', 'ccc']
                     ))