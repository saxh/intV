def countFun(cards=[]):
    count = 0
    for i in range(len(cards) - 1):
        if cards[i] > cards[i + 1]:
            count += 1
    return count


def countFun_R(cards=[]):
    count = 0
    for i in range(len(cards) - 1):
        if cards[i] < cards[i + 1]:
            count += 1
    return count


def reMove(cards):
    index = []
    for i in range(len(cards) - 1):
        if cards[i] > cards[i + 1]:
            index.append(cards[i + 1])
    for i in index:
        cards.remove(i)


def reMove_R(cards):
    index = []
    for i in range(len(cards) - 1):
        if cards[i] < cards[i + 1]:
            index.append(cards[i + 1])
    for i in index:
        cards.remove(i)


if __name__ == '__main__':
    a = int(input().strip())
    cards = list(map(int, input().strip().split(" ")))

    # print(cards)
    if a == 1:
        print(1)
        exit()
    step = 0
    while len(cards) > 1:

        count = countFun(cards)
        # cards.reverse()
        count_R = countFun_R(cards)
        # cards.reverse()
        if count >= count_R:
            reMove(cards)
        else:
            reMove_R(cards)
        step += 1
    print(step)
