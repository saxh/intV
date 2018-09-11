if __name__ == '__main__':
    ls = list(map(int, input().strip().split(" ")))
    index = 1
    lost = []
    count = 0
    while index + count < 10:
        if index != ls[index - count - 1]:
            count += 1
            lost.append(index)
        index += 1

    print(int("".join(map(str, sorted(lost)))) % 7)
