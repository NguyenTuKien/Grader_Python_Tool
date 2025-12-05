from sys import stdin

class Customer:
    def __init__ (self, id, name, old_idx, new_idx):
        self.id = "KH" + id.zfill(2)
        self.name = name
        self.total = self.cal(old_idx, new_idx)

    def cal(self, old_idx, new_idx):
        diff = new_idx - old_idx
        total = min(diff, 50) * 100
        if diff > 50:
            total += min((diff - 50), 50) * 150
        if diff > 100:
            total += (diff - 100) * 200

        if diff > 100:
            return round(total * 1.05)
        elif diff > 50:
            return round(total * 1.03)
        else:
            return round(total * 1.02)

def main():
    data = stdin.read().split("\n")
    it = iter(data)
    customers = []
    for i in range(int(next(it))):
        name = next(it).strip()
        old_idx = int(next(it).strip())
        new_idx = int(next(it).strip())
        customers.append(Customer(str(i + 1), name, old_idx, new_idx))
    customers.sort(key=lambda x: -x.total)
    for customer in customers:
        print(f"{customer.id} {customer.name} {customer.total}")

if __name__ == "__main__":
    main()