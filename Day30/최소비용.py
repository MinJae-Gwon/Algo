import sys
sys.stdin = open('최소비용.txt','r')

# 시간초과 오짐
def IsSafe(y,x):
    if y>=0 and y<N and x>=0 and x<N:
        return True

def dfs(here_y, here_x, sofar):
    global min_fuel
    if sofar >= min_fuel:
        return
    if here_y==N-1 and here_x==N-1:
        if sofar < min_fuel:
            min_fuel = sofar
        return

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    for dir in range(len(dy)):
        next_y = here_y + dy[dir]
        next_x = here_x + dx[dir]
        if IsSafe(next_y,next_x) and visited[next_y][next_x]==0:
            if data[here_y][here_x] < data[next_y][next_x] and sofar+1+(data[next_y][next_x]-data[here_y][here_x]) < mymap[next_y][next_x]:
                visited[next_y][next_x] = True
                mymap[next_y][next_x] = sofar+1+(data[next_y][next_x]-data[here_y][here_x])
                dfs(next_y,next_x,sofar+1+(data[next_y][next_x]-data[here_y][here_x]))
                visited[next_y][next_x] = 0
            elif data[here_y][here_x] >= data[next_y][next_x] and sofar+1 < mymap[next_y][next_x]:
                visited[next_y][next_x] = True
                mymap[next_y][next_x] = sofar + 1
                dfs(next_y, next_x, sofar + 1)
                visited[next_y][next_x] = 0

T = int(input())
for time in range(T):
    N = int(input())
    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    mymap = [[987654321999 for _ in range(N)] for _ in range(N)]
    mymap[0][0] = data[0][0]
    visited =[[0 for _ in range(N)] for _ in range(N)]
    visited[0][0] = True

    min_fuel = 98765432
    dfs(0,0,data[0][0])
    print('#{0} {1}'.format(time+1,min_fuel))