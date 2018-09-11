if __name__ == '__main__':
    a = input()
    max_index = 0
    start = 0
    count = 0
    max = 0
    index = 0
    while index < len(a):
        count = 0
        while index < len(a) and 9 >= ord(a[index]) - ord("0") >= 0:
            index += 1
            count += 1

        if count > max:
            max = count
            max_index = start

        start = index
        index += 1
    print(a[max_index + 1:max_index + max+1])
