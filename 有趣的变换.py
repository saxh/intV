if __name__ == '__main__':
    a = input()
    data = []
    for i in range(1, len(a)):
        # print(a[0:i], a[i:])
        x1 = a[0:i]
        x2 = a[i:]

        data.append([x1, x2])
        # data.append()
    print(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][0] = data[i][0:j] + "." + data[j:]
            
