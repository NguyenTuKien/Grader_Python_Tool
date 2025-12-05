if __name__ == '__main__':
    s = input()
    last = s[-3 : ]
    last = last.lower()
    if(last == ".py"):
        print("yes")
    else:
        print("no")
