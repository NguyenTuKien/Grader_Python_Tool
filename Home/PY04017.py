from sys import stdin

class Competitor:
    def __init__(self, name, des, time):
        self.name = name.strip()
        self.des = des.strip()
        self.time = time.strip()
        self.id = self.genId()

    def genId(self):
        name_split = self.name.split()
        des_split = self.des.split()
        id_des = ''.join([word[0].upper() for word in des_split])
        id_name = ''.join([word[0].upper() for word in name_split])
        return f"{id_des}{id_name}"

    def getV(self):
        h, m = map(int, self.time.split(':'))
        dur = (h - 6) * 60 + m
        return 120 * 60 / dur
    
    def __lt__(self, other):
        return self.getV() > other.getV()
    
    def __str__(self):
        return f"{self.id} {self.name} {self.des} {round(self.getV())} Km/h"
    
def main():
    comp = []
    for _ in range(int(stdin.readline())):
        name = stdin.readline()
        des = stdin.readline()
        time = stdin.readline()
        comp.append(Competitor(name, des, time))
        
    comp.sort()
    
    for c in comp:
        print(c)

if __name__ == '__main__':
    main()