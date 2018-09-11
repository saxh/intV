if __name__ == '__main__':
    # num, cnt = input().split(" ")
    num = list(input())
    cnt = int(input())
    i = 1
    count = 0
    checked = 0
    while count < cnt and i < len(num):
        if num[i] > num[i - 1]:
            num.pop(i - 1)
            count += 1
            i = 1
        else:
            i += 1
    if count == cnt:
        print("".join(num))
    else:
        print("".join(num[:count - cnt]))
