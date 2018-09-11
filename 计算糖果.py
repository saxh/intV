if __name__ == '__main__':
    x1, x2, x3, x4 = list(map(int, input().strip().split(" ")))
    if (x1 + x3) % 2 == 1 or (x2 + x4) % 2 == 1 or (x2 + x4) < 0:
        print("No")
        exit()
    A = (x1 + x3) // 2
    B = A - x1
    C = B - x2
    print(A, B, C)
