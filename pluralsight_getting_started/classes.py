students = []


class OldStudent:
    pass


student_1 = OldStudent()

print(student_1)

student_2 = OldStudent()
print(student_2)


class Student:
    def add_student(self, name, student_id=332):
        student = {'name': name, 'student_id': student_id}
        students.append(student)


student = Student()
student.add_student('Marc')

print(students)
