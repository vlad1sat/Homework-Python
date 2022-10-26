def tpl_sort(user_tuple):
    for number in user_tuple:
        if not isinstance(number, int):
            return user_tuple
    return tuple(sorted(user_tuple))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
