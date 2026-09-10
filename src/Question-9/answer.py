from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)

total = sum(int(Student(*input().split()).MARKS) for _ in range(n))
print(f"{total / n:.2f}")