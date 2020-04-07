import sys, math
sys.stdin = open('4301_콩심기.txt','r')

def IsSafe(y,x):
    if y>=0 and x>=0 and y<M and x<N:
        return True

def go(y,x):
    global grid

    dy = [0,2,0,-2]
    dx = [2,0,-2,0]

    for dir in range(4):
        n_y = y + dy[dir]
        n_x = x + dx[dir]

        if IsSafe(n_y,n_x):
            grid[n_y][n_x] = 0

tc = int(input())

for case in range(tc):
    N,M = map(int,input().split())
    grid = [[1 for _ in range(N)] for _ in range(M)]
    cnt=0
    for y in range(M):
        for x in range(N):
            if grid[y][x] == 1:
                go(y,x)

    for cnt_y in range(M):
        for cnt_x in range(N):
            if grid[cnt_y][cnt_x] == 1:
                cnt+=1
    print(f'#{case+1} {cnt}')

