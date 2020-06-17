import sys
sys.stdin = open('미로.txt','r')

def IsSafe(y,x):
    if y>=0 and y<N and x>=0 and x<M:
        return True

def dfs(y,x,how_far):
    global min_far

    if how_far > min_far:
        return

    if y == N-1 and x == M-1:
        if how_far < min_far:
            min_far = how_far
        return

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    for dir in range(4):
        n_y = y + dy[dir]
        n_x = x + dx[dir]
        if IsSafe(n_y,n_x):
            if maze[n_y][n_x] == 1 and visit[n_y][n_x] == 0:
                visit[n_y][n_x] = 1
                dfs(n_y,n_x,how_far+1)
                visit[n_y][n_x] = 0

N,M = map(int,input().split())

maze = []
for rows in range(N):
    row = list(map(int,list(input())))
    maze.append(row)
Q = []
visit = [[0 for _ in range(M)] for _ in range(N)]
visit[0][0] = 1
min_far = 9999999999999
dfs(0,0,1)

print(min_far)