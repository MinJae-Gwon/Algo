import sys
sys.stdin = open('보급로.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and x<N and y<N:
        return True

def go(y, x , sofar):
    global min_cost

    # pruning 매우 중요
    if sofar > min_cost:
        return

    if y == N-1 and x == N-1:
        if sofar < min_cost:
            min_cost = sofar
        return

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    for dir in range(4):
        n_y = y + dy[dir]
        n_x = x + dx[dir]
        if IsSafe(n_y,n_x) and visit[n_y][n_x] == 0 and sofar < cost_map[n_y][n_x]:
            visit[n_y][n_x] = True

            cost_map[n_y][n_x] = sofar + field[n_y][n_x]
            go(n_y,n_x,sofar + field[n_y][n_x])
            visit[n_y][n_x] = 0

T = int(input())
for time in range(T):
    N = int(input())

    field = []
    for rows in range(N):
        row = list(map(int,list(input())))
        field.append(row)
    # print(field)

    visit = [[0 for _ in range(N)] for _ in range(N)]
    cost_map = [[98765432199 for _ in range(N)] for _ in range(N)]
    visit[0][0] = True
    cost_map[0][0] = 0
    min_cost = 98765432199
    go(0,0,0)
    print('#{0} {1}'.format(time+1,min_cost))