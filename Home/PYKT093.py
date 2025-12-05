from sys import stdin
import math

class Student:
    def __init__ (self, id, name, p1, p2, p3):
        self.id = "SV" + id.zfill(2)
        self.name = name
        self.avg = math.ceil(((float(p1) * 3 + float(p2) * 3 + float(p3) * 2) / 8) * 100) / 100

def ConcatName(name):
    parts = name.strip().lower().split()
    parts = [part.capitalize() for part in parts]
    return " ".join(parts)

def main():
    students = []
    rank = 1
    for i in range(int(stdin.readline())):
        name = ConcatName(stdin.readline())
        p1 = stdin.readline().strip()
        p2 = stdin.readline().strip()
        p3 = stdin.readline().strip()
        students.append(Student(str(i + 1), name, p1, p2, p3))
    students.sort(key=lambda x: (-x.avg, x.id))
    for i, student in enumerate(students):
        if i > 0 and student.avg < students[i - 1].avg:
            rank = i + 1
        print(f"{student.id} {student.name} {student.avg:.2f} {rank}")


if __name__ == "__main__":
    main()