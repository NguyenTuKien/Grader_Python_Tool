import math

if __name__ == '__main__':
    se = {',', '.', '?', '!', ':', ';', '(', ')', '-', '/'}
    dict = {}
    tu = []

    n, k = map(int, input().split())
    for i in range(n):
        t = input()
        tmp = ""
        for i in t:
            if i in se:
                tmp += " "
            else:
                tmp += i

        a = tmp.split()
        tu.extend(a)
        for word in a:
            if word.lower() not in dict:
                dict[word.lower()] = 1
            else:
                dict[word.lower()] += 1

    # for word in tu:
    #     if dict[word.lower()] >= k:
    #         print(f'{word.lower()} {dict[word.lower()]}')
    #         dict[word.lower()] = 0




    # Sort dictionary theo value giảm dần
    sorted_dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    
    # In k từ có tần suất cao nhất
    for word, freq in sorted_dict:
        if freq >= k:
            print(f'{word} {freq}')