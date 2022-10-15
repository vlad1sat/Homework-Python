nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
flat = [number for list_2 in nice_list for list_numbers in list_2 for number in list_numbers]
print(flat)