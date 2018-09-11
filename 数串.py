import sys
from functools import cmp_to_key


def mycmp(x, y):
    if x + y > y + x:
        return 1
    elif x == y:
        return 0
    else:
        return -1


if __name__ == '__main__':
    n = int(input())
    b = list(input().split(" "))
    b.sort(reverse=True, key=cmp_to_key(mycmp))
    print("".join(b))
    # print("9479469393936860828217727587256726664963660859057255453552352241339937934431330729291210204184178153123115")
