import csv

# students = []
# with open('students.csv', 'r') as file:
#     reader = csv.reader(file)
#     for line in reader:
#         students.append({'name': line[0], 'company': line[1]})
#
#
# for student in sorted(students, key=lambda student: student['name']):
#     print(f'{student["name"]} works at {student["company"]}')


# -----------------------------------------------------------

# dict reader
# students = []
# with open('students_dict.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for line in reader:
#         students.append({'name': line['name'], 'company': line["company"]})
#
#
# for student in sorted(students, key=lambda student: student['name']):
#     print(f'{student["name"]} works at {student["company"]}')

# dict writer

name = input('what your name? ')
company = input('where doo you wirk at? ')

with open('students.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'company'])
    writer.writerow({'name': name, 'company': company})

