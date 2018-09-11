if __name__ == '__main__':
    a = int(input().strip())
    x = list(map(int, input().strip().split(" ")))
    y = list(map(int, input().strip().split(" ")))
    s = [x[i] + y[i] for i in range(a)]
    print(min(s) - 2)
