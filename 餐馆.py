def search(start=0, end=100, aim=10, capbility=[], vis=[]):
    while start < end:
        mid = (start + end) // 2
        if vis[mid]:
            mid += 1
        pre = mid - 1
        if pre >= 0 and vis[pre] == True:
            pre -= 1

        if capbility[mid] >= aim and (pre == -1 or capbility[pre] < aim):
            return mid
        elif capbility[mid] < aim:
            return search(mid + 1, end, aim, capbility, vis)
        else:
            return search(start, mid - 1, aim, capbility, vis)
    if start == end and capbility[start] >= aim and vis[start] == False:
        return start
    return -1


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split(" ")))
    capbility = list(map(int, input().strip().split(" ")))
    consumer = []
    for i in range(m):
        consumer.append(list(map(int, input().strip().split(" "))))
    capbility.sort()
    consumer.sort(key=lambda consumer: consumer[1], reverse=True)
    # print(capbility)
    # print(consumer)
    vis = [False] * n
    sum = 0
    for i in range(m):
        if vis.__contains__(False):
            index = search(0, n - 1, consumer[i][0], capbility, vis)

            if index != -1:
                vis[index] = True
                sum += consumer[i][1]

    print(sum)
    # 3 5
    # 2 4 2
    # 1 3
    # 3 5
    # 3 7
    # 5 9
    # 1 10
