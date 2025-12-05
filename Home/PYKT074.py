from sys import stdin


def main():
    for _ in range(int(stdin.readline())):
        line = stdin.readline()
        words = line.split()
        res = [] 
        current_len = 0 
        for word in words:
            word_len = len(word)
            cost = word_len + (1 if res else 0)
            if current_len + cost <= 100:
                res.append(word)
                current_len += cost
            else:
                break
        print(" ".join(res))         


if __name__ == "__main__":
    main()