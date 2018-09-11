if __name__ == '__main__':
    try:
        s = list(map(int, input().strip().split(" ")))
        # print(int("100",base=9))
        print(sum(s))
    except:
        print("error")
