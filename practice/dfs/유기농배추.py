import sys
sys.stdin = open('유기농배추.txt','r')

def IsSafe(y,x):
    if x>=0 and x <M and y>=0 and y<N:
        return True

def bfs(here_y, here_x):
    global cnt
    visited[here_y][here_x] =True
    Q.append(here_y)
    Q.append(here_x)

    dy = [0,-1,0,1]
    dx = [-1,0,1,0]
    while Q:
        now_y = Q.pop(0)
        now_x = Q.pop(0)

        for dir in range(len(dy)):
            next_y = now_y + dy[dir]
            next_x = now_x + dx[dir]
            if IsSafe(next_y,next_x) and data[next_y][next_x] == 1 and visited[next_y][next_x] ==0:
                visited[next_y][next_x] = True
                Q.append(next_y)
                Q.append(next_x)
    cnt+=1



T = int(input())
for time in range(T):
    M,N,K = map(int,input().split())
    data=[[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    Q=[]
    cnt=0

    for info in range(K):
        x,y = map(int,input().split())
        data[y][x] = 1

    for y_idx in range(N):
        for x_idx in range(M):
            if data[y_idx][x_idx] ==1 and visited[y_idx][x_idx]==0:
                bfs(y_idx,x_idx)
    print(cnt)