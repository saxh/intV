if __name__ == '__main__':
    a = int(input().strip())
    s = list(map(int, input().strip().split(" ")))
    count = 0
    for i in range(a):
        if 1 ^ s[i] == 0:
            count += 1
    print((count-1)*(a-count+1))
