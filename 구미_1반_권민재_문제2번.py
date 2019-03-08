import sys
sys.stdin = open('2번.txt','r')

def Issafe(y,x):
    if x >=0 and x < N and y >=0 and y < N:
        return True
def Ispossible(y,x):
    if data[y][x] != 0:
        return True

def IsNotVisited(y,x):
    if visited[y][x] ==0:
        return True

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(start_y, start_x):
    global Q, dx, dy, cnt
    Q.append(start_y)
    Q.append(start_x)
    visited[start_y][start_x] = True
    while Q:
        here_y = Q.pop(0)
        here_x = Q.pop(0)
        for dir in range(len(dy)):

            next_y = here_y + dy[dir]
            next_x = here_x + dx[dir]
            if Issafe(next_y,next_x) and Ispossible(next_y,next_x) and IsNotVisited(next_y,next_x):
                visited[next_y][next_x] = True
                Q.append(next_y)
                Q.append(next_x)
    cnt+=1


T = int(input())
for time in range(T):
    N = int(input())
    data = []
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    visited = [[0 for _ in range(N)] for _ in range(N)]
    Q=[]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if data[y][x] and visited[y][x] ==0:
                bfs(y,x)
    max_h = 0
    for y_idx in range(N):
        for x_idx in range(N):
            h = data[y_idx][x_idx]
            if h > max_h:
                max_h = h

    print('#{0} {1} {2}'.format(time+1,cnt,max_h))