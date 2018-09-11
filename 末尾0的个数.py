if __name__ == '__main__':
    n = int(input())
    sum = 0
    while n > 0:
        n = n // 5
        sum += n
    print(sum)
