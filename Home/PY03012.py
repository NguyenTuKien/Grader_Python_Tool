from sys import stdin


def main():
    dict = {}
    for _ in range(int(stdin.readline())):
        name = stdin.readline().strip()
        score, total = map(int, stdin.readline().split())
        if name not in dict:
            dict[name] = [0, 0]
        dict[name][0] += score
        dict[name][1] += total
    sorted_dict = sorted(dict.items(), key=lambda x: (-x[1][0], x[1][1], x[0]))
    for name, (score, total) in sorted_dict:
        print(f"{name} {score} {total}")

if __name__ == "__main__":
    main()