def filter_users(users_filter, filter_name):
    other_filter = filter_name + 'а'
    for full_name, age in users_filter.items():
        if filter_name in full_name or other_filter in full_name:
            print(full_name[0], full_name[1], age)


users = {
    ("Сидоров", "Никита"): 35,
    ("Бубенцов", "Алексей"): 35,
    ("Сидорова", "Алина"): 34,
    ("Новиков", "Илья"): 35,
    ("Сидоров", "Павел"): 10
}

surname = input("Введите фамилию: ")
filter_users(users, surname)