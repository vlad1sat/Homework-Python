def slicer(user_tuple, number):
    if number not in user_tuple:
        return tuple()
    new_list = list()
    is_end = False
    for element_tuple in user_tuple:
        if not element_tuple == number:
            if not is_end:
                continue
            new_list.append(element_tuple)
        else:
            new_list.append(element_tuple)
            if is_end:
                break
            is_end = True
    return tuple(new_list)


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
