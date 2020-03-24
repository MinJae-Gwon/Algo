import sys
sys.stdin = open('숫자이어붙이기.txt','r')


def IsSafe(y,x):
    if y >=0 and x>=0 and y <4 and x<4:
        return True

def go(y,x,deep,word):
    global res

    if deep == 6:
        if word not in res:
            res.append(word)
        return

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    for dir in range(4):
        n_y = y + dy[dir]
        n_x = x + dx[dir]

        if IsSafe(n_y,n_x):
            go(n_y,n_x,deep+1,word+field[n_y][n_x])



case = int(input())
for tc in range(case):
    field = []

    for _ in range(4):
        row = input().split()
        field.append(row)

    #print(field)

    res = []
    for start_y in range(4):
        for start_x in range(4):
            go(start_y, start_x,0,field[start_y][start_x])


    print('#{} {}'.format(tc+1,len(res)))