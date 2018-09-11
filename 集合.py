if __name__ == '__main__':
    n, m = list(map(int, input().split(" ")))
    s1 = set(map(int, input().split(" ")))
    s2 = set(map(int, input().split(" ")))
    s = s1.union(s2)
    s = sorted(list(s))
    print(" ".join(map(str,s)))
