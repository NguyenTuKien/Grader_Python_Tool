from sys import stdin
from datetime import datetime


class ExamShift:
    def __init__ (self, id, date, time, room):
        self.id = "C" + id.zfill(3)
        self.date = date
        self.time = time
        self.room = room

def main():
    with open("CATHI.in") as f:
        examShifts = []
        for i in range(int(f.readline())):
            date = f.readline().strip()
            time = f.readline().strip()
            room = f.readline().strip()
            examShifts.append(ExamShift(str(i+1), date, time, room))    
        examShifts.sort(key=lambda x: (datetime.strptime(x.date, "%d/%m/%Y"), datetime.strptime(x.time, "%H:%M")))
        for shift in examShifts:
            print(f"{shift.id} {shift.date} {shift.time} {shift.room}")

if __name__ == "__main__":
    main()