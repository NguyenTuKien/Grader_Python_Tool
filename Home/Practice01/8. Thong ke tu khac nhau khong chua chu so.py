import re

n = int(input())
freq = {}

for _ in range(n):
    words = re.split(r'[^a-zA-Z0-9]+', input())
    for w in words:
        if w.isnumeric():
            freq[w] = freq.get(w, 0) + 1
        elif w == '':
            continue
        else:
            w = w.lower()
            freq[w] = freq.get(w, 0) + 1
    sorted_items = sorted(freq.items(), key = lambda x: (-x[1], x[0]))
for w, cnt in sorted_items:
    print(w, cnt)