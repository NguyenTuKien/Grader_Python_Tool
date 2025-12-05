from sys import stdin
import datetime

class Customer:
    def __init__ (self, id, name, room, arrival_date, return_date, fee):
        self.id = "KH" + id.zfill(2)
        self.name = name
        self.room = room
        self.days = (return_date - arrival_date).days + 1
        self.fee = fee
        self.total = self.cal_total(fee)

    def cal_total(self, fee):
        if self.room[0] == '1':
            return self.days * 25 + fee
        elif self.room[0] == '2':
            return self.days * 34 + fee
        elif self.room[0] == '3':
            return self.days * 50 + fee
        else:
            return self.days * 80 + fee

def main():
    data = stdin.buffer.read().split("\n".encode())
    it = iter(data)
    customers = []
    for i in range(int(next(it))):
        name = next(it).decode().strip()
        room = next(it).decode().strip()
        arrival_date = datetime.datetime.strptime(next(it).decode().strip(), "%d/%m/%Y")
        return_date = datetime.datetime.strptime(next(it).decode().strip(), "%d/%m/%Y")
        fee = int(next(it).decode().strip())
        customers.append(Customer(str(i + 1), name, room, arrival_date, return_date, fee))
    customers.sort(key=lambda x: -x.total)
    for customer in customers:
        print(f"{customer.id} {customer.name} {customer.room} {customer.days} {customer.total}")

if __name__ == "__main__":
    main()