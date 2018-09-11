def is_reverse(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()
    count = 0
    for i in range(len(a)+1):
        s = a[0:i] + b + a[i:]
        if is_reverse(s):
            count += 1
    print(count)
