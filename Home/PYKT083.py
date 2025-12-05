import sys

def main():
    price_map = {
        ("Xe_con", 5): 10000,
        ("Xe_con", 7): 15000,
        ("Xe_tai", 2): 20000,
        ("Xe_khach", 29): 50000,
        ("Xe_khach", 45): 70000
    }
    daily_totals = {}
    n = int(sys.stdin.readline())
    for _ in range(n):
        line = sys.stdin.readline().split()
        loai_xe = line[1]
        so_ghe = int(line[2]) 
        direction = line[3]
        date = line[4]
        if direction == "IN":
            lookup_key = (loai_xe, so_ghe)
            fee = price_map.get(lookup_key, 0)
            daily_totals[date] = daily_totals.get(date, 0) + fee
    for date, total in daily_totals.items():
        print(f"{date}: {total}")

if __name__ == "__main__":
    main()