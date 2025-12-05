from sys import stdin

def main():
    input_data = stdin.read().split()
    it = iter(input_data)
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    min_steps = float('inf') 
    chosen_val = -1
    for target in a:
        current_steps = 0
        for x in a:
            current_steps += abs(x - target)
        if current_steps < min_steps:
            min_steps = current_steps
            chosen_val = target
    print(min_steps, chosen_val)

if __name__ == "__main__":
    main()