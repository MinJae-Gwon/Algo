import sys
sys.stdin = open('맥주.txt','r')

def IsPossible(y,x,n_y,n_x):
    dist = abs(n_y - y) + abs(n_x - x)

    if dist <= 1000:
        return True
    else:
        return False

def bfs(data):
    global can_go

    start_y = data[0]
    start_x = data[1]

    if IsPossible(start_y,start_x, penta_y, penta_x):
        can_go = True
        return


    for i in range(0,N):
        next_y = combinis[i][0]
        next_x = combinis[i][1]

        if visit[i] == 0 and IsPossible(start_y, start_x, next_y, next_x):
            visit[i] = 1
            bfs(combinis[i])
            visit[i] = 0



T = int(input())

for case in range(T):
    N = int(input())
    combinis = []
    home_y, home_x = map(int,input().split())
    home = (home_y, home_x)

    for combinis_data in range(N):
        combini_y, combini_x = map(int,input().split())
        combini = (combini_y, combini_x)
        combinis.append(combini)

    penta_y, penta_x = map(int,input().split())
    penta = (penta_y, penta_x)

    visit = [0 for _ in range(N)]

    can_go = False

    bfs(home)

    if can_go:
        print('happy')
    else:
        print('sad')