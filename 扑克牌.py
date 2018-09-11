if __name__ == '__main__':
    a = list(input())
    ls = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "T", "J", "Q", "K"]
    a = [ls.index(i) for i in a]
    a.sort()
    print(a)
