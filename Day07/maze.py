import sys
sys.stdin = open('maze.txt','r')

def Issafe(x,y):
    if x>=0 and x<N and y>=0 and y<N:
        return True
def Ispossible(x,y):
    if data[y][x] !=1:
        return True
def IsNotVisited(x,y):
    if data[y][x] != -1:
        return True
ans=0
def pathfinder(x,y):
    global ans
    data[y][x]=-1
    if x==end_x and y==end_y:
        ans = 1
        return
    for dir in range(len(dx)):
        new_start_x = x + dx[dir]
        new_start_y = y + dy[dir]
        if Issafe(new_start_x,new_start_y) and Ispossible(new_start_x,new_start_y) and IsNotVisited(new_start_x,new_start_y):
            pathfinder(new_start_x,new_start_y)

T = int(input())
for time in range(T):
    N = int(input())
    data = []
    for rows in range(N):
        row = list(map(int,input()))
        data.append(row)
    # delta
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    #startpoint
    for start_y_idx in range(N):
        for start_x_idx in range(N):
            if data[start_y_idx][start_x_idx]==3:
                start_x = start_x_idx
                start_y = start_y_idx
    # endpoint
    for end_y_idx in range(N):
        for end_x_idx in range(N):
            if data[end_y_idx][end_x_idx]==2:
                end_x = end_x_idx
                end_y = end_y_idx
    pathfinder(start_x,start_y)
    print(f'#{time+1} {ans}')
    ans=0
