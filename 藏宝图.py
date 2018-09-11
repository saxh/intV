if __name__ == '__main__':
    a = list(input())
    b = list(input())
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(b):
        print("Yes")
    else:
        print("No")
