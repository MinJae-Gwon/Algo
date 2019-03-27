import sys
sys.stdin = open('디저트.txt','r')

def IsSafe(y,x):
    if x>=0 and x<N and y>=0 and y<N:
        return True

def dfs(here_y, here_x,status):
    global res,y,x
    if here_y == y and here_x == x and start_flag==False:
        res.append(sum(eaten_dessert))
        return

    dy = []
    dx = []

    for dir in range(len(dy)):
        next_y = here_y+dy[dir]
        next_x = here_x+dx[dir]



T = int(input())
for time in range(T):
    N = int(input())
    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    res=[]
    for y in range(N):
        for x in range(N):
            eaten_dessert = [0]*(101)
            eaten_dessert[data[y][x]] =1
            start_flag=True
            dfs(y,x,1)
    print(res)