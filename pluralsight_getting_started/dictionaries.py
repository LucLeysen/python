student = {
    'name': 'Mark',
    'student_id': 15163,
    'feedback': None
}

all_students = [
    {'name': 'Mark', 'student_id': 15163},
    {'name': 'Karla', 'student_id': 63112},
    {'name': 'Jessica', 'student_id': 30021},
]

for student_listed in all_students:
    print(student_listed['name'])

print(student['name'])

# print(student['last_name']) # KeyError

print(student.get('last_name', 'unknown'))

print(student.keys())
print(student.values())

del student['name']

print(student.keys())
print(student.values())
