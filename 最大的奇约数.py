def count(a=1000000000):
    global sum
    if a == 1:
        sum += 1
        return

    sum += ((a + 1) // 2) * ((1 + a) // 2)

    count(a // 2)


if __name__ == '__main__':
    a = input()
    sum = int(0)
    count(int(a))
    print(int(sum))
