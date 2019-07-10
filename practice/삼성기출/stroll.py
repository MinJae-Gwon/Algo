import sys
sys.stdin = open('stroll.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and y<N and x<N:
        return True

def high():
    max_high=0
    for y in range(N):
        for x in range(N):
            if data[y][x] > max_high:
                max_high = data[y][x]
    return max_high

def no_way(y,x):
    global visited
    deadlock = True
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    for check_dir in range(len(dy)):
        check_y = y + dy[check_dir]
        check_x = x + dx[check_dir]
        if IsSafe(check_y, check_x) and visited[check_y][check_x] == 0:
            if data[check_y][check_x] < data[y][x]:
                deadlock = False
                break

    return deadlock

def dfs(y,x,sofar):
    global visited, max_sofar

    if no_way(y,x):
        if sofar > max_sofar:
            max_sofar = sofar
        return

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    for dir in range(len(dy)):
        n_y = y + dy[dir]
        n_x = x + dx[dir]
        if IsSafe(n_y, n_x) and visited[n_y][n_x] == 0 and data[n_y][n_x] < data[y][x]:
            visited[n_y][n_x] = True
            dfs(n_y,n_x,sofar+1)
            visited[n_y][n_x] = 0


def go():
    global visited, max_sofar
    high_point = high()

    for y in range(N):
        for x in range(N):
            if data[y][x] == high_point:
                visited=[[0 for _ in range(N)] for _ in range(N)]
                visited[y][x]=True
                dfs(y,x,1)



T = int(input())
for time in range(T):
    N,K = map(int,input().split())
    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    max_sofar = 1
    for y in range(N):
        for x in range(N):
            for deep in range(K+1):
                data[y][x] = data[y][x]-deep
                go()
                data[y][x] = data[y][x]+deep

    print('#{0} {1}'.format(time+1,max_sofar))