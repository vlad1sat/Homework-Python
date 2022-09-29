def max_determinant(first_number, second_number):
    if first_number == 0 or second_number == 0:
        return
    result = 1
    for determinant in range(2, min(first_number, second_number) + 1):
        if first_number % determinant == 0 and second_number % determinant == 0:
            result = determinant
    return result
