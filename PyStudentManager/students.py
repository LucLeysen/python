students = []


def get_student_title_case():
    student_title_case = []
    for student in students:
        student_title_case.append(student['name'].title())
    return student_title_case


def print_student_title_case():
    student_title_case = get_student_title_case()
    print(student_title_case)


def add_student(name, student_id=100):
    student = {'name': name, 'student_id': student_id}
    students.append(student)


def save_file(student):
    try:
        f = open('students.txt', 'a')
        f.write(student + '\n')
        f.close()
    except Exception:
        print('Could not read file.')


def read_file():
    try:
        f = open('students.txt', 'r')
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print('Could not read file.')


read_file()
print_student_title_case()

student_name = input('Enter student name: ')
student_id = input('Enter student id: ')

add_student(student_name, student_id)
save_file(student_name)
