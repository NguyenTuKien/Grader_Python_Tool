from sys import stdin

class TeamResult:
    def __init__(self, name: str, points: int, diff : int, goals: int):
        self.name = name
        self.points = points
        self.diff = diff
        self.goals = goals


    def __lt__ (self, other) :
        return (-self.points, -self.diff, -self.goals, self.name) < (-other.points, -other.diff, -other.goals, other.name)

    def __str__(self):
        return f"{self.name} {self.points} {self.diff} {self.goals}"

def main():
    teams = []
    for _ in range(int(stdin.readline().strip())):
        name = stdin.readline().strip()
        points, diff, goals = map(int, stdin.readline().strip().split())
        teams.append(TeamResult(name, points, diff, goals))
    teams.sort()
    for team in teams:
        print(team)
        
if __name__ == "__main__":
    main()