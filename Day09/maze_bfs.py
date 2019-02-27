import sys
sys.stdin = open('maze_bfs.txt','r')

def Issafe(y,x):
    if x>=0 and x<N and y>=0 and y<N:
        return True
def Ispossible(y,x):
    if data[y][x] != 1:
        return True
def Isnotvisited(y,x):
    if data[y][x] != -1:
        return True

def bfs(y,x):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    Q.append((y,x))
    data[y][x] = -1
    while Q:
        here_y, here_x = Q.pop(0)
        for dir in range(len(dx)):
            new_y = here_y + dy[dir]
            new_x = here_x + dx[dir]
            if Issafe(new_y,new_x) and Ispossible(new_y,new_x) and Isnotvisited(new_y,new_x):
                Q.append((new_y,new_x))
                data[new_y][new_x] = -1
            if data[new_y][new_x] == 3:
                return 1
    return 0

T = int(input())
for time in range(T):
    N = int(input())
    data = []
    for rows in range(N):
        row = [int(ele) for ele in list(input())]
        data.append(row)
    Q=[]
    # start
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                start_y = y
                start_x = x
    print(bfs(start_y,start_x))
