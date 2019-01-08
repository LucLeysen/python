students = []


def add_student(name, student_id=None):
    student = {'name': name, 'student_id':student_id}
    students.append(student)


add_student('Marc')
add_student(name='Jeff', student_id=123)

print(students)


def var_args(name, *args):
    print(name)
    print(args)


var_args('Luke', 'pike', 'perch', 'zander', 126, False)


def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs['description'], kwargs['feedback'])


var_kwargs('Luke', description='Loves Python', feedback=None, pluralsight_subscriber=True)
