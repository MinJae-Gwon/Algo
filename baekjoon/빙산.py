import sys
sys.stdin = open('빙산.txt', 'r')


def IsSafe(y,x):
    if y>=0 and y<N and x>=0 and x<M:
        return True

def contact(y,x):
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    cnt = 0

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if IsSafe(ny,nx) and sea[ny][nx] == 0:
            cnt+=1

    return cnt


def melt():
    c_sea = [[0 for _ in range(M)] for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if sea[y][x] == 0:
                continue
            else:
                sides = contact(y,x)

                if sea[y][x] - sides < 0:
                    c_sea[y][x] = 0
                else:
                    c_sea[y][x] = sea[y][x] - sides
    return c_sea

def divid(y,x):
    Q.append(y)
    Q.append(x)

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while Q:
        y = Q.pop(0)
        x = Q.pop(0)

        for dir in range(4):
            n_y = y + dy[dir]
            n_x = x + dx[dir]

            if IsSafe(n_y,n_x) and sea[n_y][n_x] != 0 and visit[n_y][n_x] == 0:
                visit[n_y][n_x] = 1
                Q.append(n_y)
                Q.append(n_x)


N,M = map(int,input().split())

sea = []
for rows in range(N):
    row = list(map(int,input().split()))
    sea.append(row)

res = 0
while True:
    sea = melt()

    Q = []
    visit = [[0 for _ in range(M)] for _ in range(N)]
    how_many_islands = 0
    for i in range(N):
        for j in range(M):
            if sea[i][j] != 0 and visit[i][j] == 0:
                visit[i][j] = 1
                divid(i,j)
                how_many_islands +=1

    if how_many_islands >1:
        res += 1
        break

    if not how_many_islands:
        res = 0
        break

    res +=1

print(res)