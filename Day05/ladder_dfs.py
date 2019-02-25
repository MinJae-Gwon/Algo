import sys
sys.stdin = open('ladder_dfs.txt', 'r')

def Issafe(x,y):
    if x>=0 and x<100:
        return True
def Ispossible(x,y):
    if data[y][x] != 0:
        return True
def IsNotVisited(x,y):
    if data[y][x] != -1:
        return True
ans=0
def pathfinder(x,y):
    global ans
    if y == 0:
        ans = x
        return
    dy = [0,0,-1]
    dx = [-1,1,0]
    for idx in range(len(dx)):
        new_start_x = x + dx[idx]
        new_start_y = y + dy[idx]
        if Issafe(new_start_x,new_start_y) and Ispossible(new_start_x,new_start_y) and IsNotVisited(new_start_x,new_start_y):
            data[y][x] = -1
            pathfinder(new_start_x,new_start_y)
            return

for time in range(10):
    T = int(input())
    data = []
    for rows in range(100):
        row = list(map(int,input().split()))
        data.append(row)
    # startpoint
    for find_start in range(100):
        if data[99][find_start] == 2:
            start_x = find_start
    start_y = 99

    # path
    pathfinder(start_x,start_y)
    print(ans)
    ans=0

