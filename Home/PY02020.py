
from sys import stdin

def main():
    input_data = stdin.read().split()
    n = int(input_data[0])
    scores = [float(x) for x in input_data[1:]]
    max_val = max(scores)
    min_val = min(scores)
    filtered_scores = [x for x in scores if x != max_val and x != min_val]
    if filtered_scores:
        avg = sum(filtered_scores) / len(filtered_scores)
        print(f"{avg:.2f}")
    else:
        print("0.00")

if __name__ == "__main__":
    main()