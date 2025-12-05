from sys import stdin

class Student:
    def __init__ (self, id, name, clss):
        self.id = id
        self.name = name
        self.clss = clss

    def __str__ (self):
        return self.id + " " + self.name + " " + self.clss
    
class Attendence:
    def __init__ (self, student, attList):
        self.student = student
        self.score = self.getScore(attList)
    
    def check(self):
        if self.score == 0:
            return " KDDK"
        else :
            return ""
        
    def getScore(self, attList):
        score = 10
        for x in attList:
            if x == 'v':
                score -= 2
            elif x == 'm':
                score -= 1
        return max(score, 0)
    
    def __lt__ (self, other):
        return self.score < other.score

    def __str__ (self):
        return str(self.student) + " " + str(self.score) + self.check();

def main():
    n = int(stdin.buffer.readline())
    studentOrder = []
    students = {}
    for i in range(n):
        id = stdin.buffer.readline().decode().strip()
        name = stdin.buffer.readline().decode().strip()
        clss = stdin.buffer.readline().decode().strip()
        students[id] = Student(id, name, clss) 
        studentOrder.append(id)
    attendences = {}
    for i in range(n):
        id, attList = map(str, stdin.buffer.readline().decode().split(" "))
        attendences[id] = Attendence(students[id], attList)
    for id in studentOrder:
        print(str(attendences[id]))

if __name__ == "__main__":
    main()