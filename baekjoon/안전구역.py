import sys
sys.stdin = open('안전구역.txt','r')

def IsSafe(y,x):
    if y>=0 and y<N and x>=0 and x<N:
        return True

def flood(alt):
    for y in range(N):
        for x in range(N):
            if grid[y][x] <=alt:
                safe_grid[y][x] = 0

def bfs(y,x):
    Q.append(y)
    Q.append(x)

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    while Q:
        y = Q.pop(0)
        x = Q.pop(0)

        for dir in range(4):
            n_y = y + dy[dir]
            n_x = x + dx[dir]

            if IsSafe(n_y,n_x) and safe_grid[n_y][n_x] ==1 and visit[n_y][n_x] == False:
                visit[n_y][n_x] = True
                Q.append(n_y)
                Q.append(n_x)


N = int(input())
grid = []

high_ground = 0
for rows in range(N):
    row = list(map(int,input().split()))
    max_ground = max(row)
    if max_ground > high_ground:
        high_ground = max_ground
    grid.append(row)

max_safe_zone_cnt = 0
for alt in range(0,high_ground+1):
    safe_grid = [[1 for _ in range(N)] for _ in range(N)]
    flood(alt)

    safe_zone_cnt = 0
    Q = []
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if safe_grid[i][j] == 1 and visit[i][j] == False:
                visit[i][j] = True
                bfs(i,j)
                safe_zone_cnt +=1

    if safe_zone_cnt > max_safe_zone_cnt:
        max_safe_zone_cnt = safe_zone_cnt

print(max_safe_zone_cnt)