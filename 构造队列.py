from collections import deque

if __name__ == '__main__':
    a = input()
    for i in range(int(a)):
        n = int(input())
        q = deque()
        for j in range(n, 0, -1):
            q.appendleft(j)
            q.appendleft(q.pop())
        print(" ".join(map(str,list(q))))
