def check(begin, end, s=[4, 1, 1, 1, 3], count=0):
    if begin >= end:
        print (count)
        return
    if s[begin] == s[end]:
        count = check(begin + 1, end - 1, s, count)
    if s[begin] < s[end]:
        s[begin + 1] = s[begin] + s[begin + 1]
        begin += 1
        count += 1
        check(begin, end, s, count)
    elif s[begin] > s[end]:
        s[end - 1] = s[end] + s[end - 1]
        end -= 1
        count += 1
        check(begin, end, s, count)


if __name__ == '__main__':
    a = list(map(int, input().strip().split(" ")))
    check(1, len(a)-1)
    # print(count)
