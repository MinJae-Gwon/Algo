import sys
sys.stdin = open('ladder2.txt','r')

def IsSafe(x,y):
    if x>=0 and x<100 and y>=0 and y<100:
        return True

def IsNotVisited(x,y):
    if not visited[y][x]:
        return True

def Ispossible(x,y):

    if data[y][x] == 1:
        return True

def dfs(here_y, here_x, sofar):
        global route,min_route

        if here_y == 0:
            route[here_x] = sofar
            return

        dx = [-1,1,0]
        dy = [0,0,-1]
        for dir in range(len(dx)):
            next_x = here_x + dx[dir]
            next_y = here_y + dy[dir]

            if IsSafe(next_x,next_y) and IsNotVisited(next_x,next_y) and Ispossible(next_x,next_y):

                visited[next_y][next_x] = 1
                dfs(next_y,next_x, sofar+1)
                return

for time in range(10):
    testcase = int(input())
    data = []
    for rows in range(100):
        row = list(map(int,input().split()))
        data.append(row)

    route = [0] * 100

    for start in range(len(data)):
       if data[99][start] == 1:

            visited = [[0 for _ in range(100)] for _ in range(100)]
            visited[99][start] = 1
            dfs(99, start, 0)

    min_route = 987654321
    for idx in range(99,-1,-1):
        if route[idx] != 0 and route[idx] < min_route:
            min_route = route[idx]
            min_idx = idx
    print('#{0} {1}'.format(time+1,min_idx))


