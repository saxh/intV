def decode(s):
    n0, n2, n6, n8, n4 = s.count("Z"), s.count("W"), s.count("X"), s.count("G"), s.count("U")
    n1, n7, n3 = s.count("O") - n0 - n2, s.count("S") - n6, s.count("T") - n8 - n2
    n9 = (s.count("N") - n1 - n7) // 2
    n5 = s.count("F") - n4
    print("0" * n8, "1" * n9, "2" * n0, "3" * n1, "4" * n2, "5" * n3, "6" * n4, "7" * n5, "8" * n6, "9" * n7, sep="")


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        decode(s)
