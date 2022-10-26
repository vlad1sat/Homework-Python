students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def get_id_age(dict_students):
    ages = []
    for id_student, information_student in dict_students.items():
        ages.append((id_student, information_student.get('age')))
    print("Список пар \"ID студента — возраст\":", ages)


def get_information(dict_student):
    interests = []
    len_surname = 0
    for id_student, information_student in dict_student.items():
        for interest in information_student.get('interests'):
            interests.append(interest)
        len_surname += len(information_student.get('surname'))
    print("Полный список интересов всех студентов:", set(interests))
    print("Общая длина всех фамилий студентов:", len_surname)


get_id_age(students)
get_information(students)
