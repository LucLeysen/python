student_names = ['Jeff', 'Tom', 'Anke']

print(student_names[0])
print(student_names[-1])

student_names[0] = 'James'

print(student_names)

student_names.append('Homer')
print(student_names)

if 'Anke' in student_names:
    print('Anke is still there')

print(len(student_names))

student_names.append(5.0)

print(student_names)

student_names.remove(5.0)

print(student_names)

del student_names[3]

print(student_names)

print(student_names[1:])
print(student_names[1:-1])
