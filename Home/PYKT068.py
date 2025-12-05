from sys import stdin

class Subject:
    def __init__ (self, id, name, method):
        self.id = id
        self.name = name
        self.method = method

def main():
    subjects = []
    for _ in range(int(stdin.readline())):
        id = stdin.readline().strip()
        name = stdin.readline().strip()
        method = stdin.readline().strip()
        subjects.append(Subject(id, name, method))
    subjects.sort(key=lambda x: x.id)
    for subject in subjects:
        print(f"{subject.id} {subject.name} {subject.method}")

if __name__ == "__main__":
    main()