student_names = ['James', 'Karla', 'Jessica', 'Mark', 'Bort', 'Frank Grimes', 'Max Power']

for name in student_names:
    if name == 'Mark':
        print('Found him! ' + name)
        break
    print('Currently testing ' + name)

for name in student_names:
    if name == 'Bort':
        continue
    print('Currently testing ' + name)
