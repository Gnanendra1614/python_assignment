from collections import namedtuple


def find_average_marks(students):
    columns = students[0]
    Student = namedtuple('Student', columns)

    total = sum(int(Student(*student).MARKS) for student in students[1:])

    return total / (len(students) - 1)