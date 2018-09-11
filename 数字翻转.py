def rev(a="123"):
    res = [i for i in a]
    res.reverse()
    res = "".join(res)
    return int(res)


if __name__ == '__main__':
    a, b = input().strip().split(" ")
    a = rev(a)
    b = rev(b)
    print(rev(str(a + b)))
