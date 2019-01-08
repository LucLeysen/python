number = 5

if number == 5:
    print('Number is 5')
else:
    print('Number is not 5')

if number:
    print('number is defined and truthy')

text = 'Python'

if text:
    print('text is defined and truthy')

python_course = True

if python_course:
    print('This will execute')

aliens_found = None

if aliens_found:
    print('Will not execute')

listing = ['a', 'b', 'c']

if listing:
    print('the listing has items')

number = 6

if number != 5:
    print('number is not 5')

java_course = False

if not java_course:
    print('not a Java course')

number = 3
python_course = True

if number == 3 and python_course:
    print('number is 3 and a python_course')

if number == 7 or python_course:
    print('number is 7 or it is a python_course')

a = 1
b = 2

print('bigger' if a > b else 'smaller')
