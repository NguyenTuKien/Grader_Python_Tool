from sys import stdin

class Order:
    def __init__ (self, id, product, quantity, price, discount):
        self.id = id
        self.product = product
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.total = quantity * price - discount

def main():
    Orders = []
    for _ in range(int(stdin.readline())):
        id = stdin.readline().strip()
        product = stdin.readline().strip()
        quantity = int(stdin.readline().strip())
        price = int(stdin.readline().strip())
        discount = int(stdin.readline().strip())
        Orders.append(Order(id, product, quantity, price, discount))
    Orders.sort(key=lambda x: -x.total)
    for order in Orders:
        print(f"{order.id} {order.product} {order.quantity} {order.price} {order.discount} {order.total}")

if __name__ == "__main__":
    main()