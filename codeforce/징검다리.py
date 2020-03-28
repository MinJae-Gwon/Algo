def can_go(i):
    global stone, jump
    gap = 0
    while True:
        if stone[i] == 0:
            gap += 1
            i += 1
        else:
            break

        if i == len(stone):
            break

    if gap > jump:
        return -1
    else:
        return gap


def go():
    global stone, jump
    flag = True
    i = 0
    while True:
        if stone[i] > 0:
            stone[i] -= 1
            i += 1
        else:
            gap = can_go(i)
            if gap == -1:
                return False
            if gap > 0:
                i += gap
        if i == len(stone):
            break
    return True



stone = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
jump = 3
answer = 0

while True:
    T_or_F = go()

    if T_or_F:
        answer += 1
    else:
        break

print(answer)