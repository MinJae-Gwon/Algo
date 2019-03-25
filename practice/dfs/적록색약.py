#백준 10026번

import sys
sys.setrecursionlimit(10000)
sys.stdin = open('적록색약.txt','r')

def IsSafe(y,x):
    if x>=0 and x<N and y>=0 and y<N:
        return True

def normal(here_y,here_x,color):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    for dir in range(len(dy)):
        next_y = here_y + dy[dir]
        next_x = here_x + dx[dir]
        if IsSafe(next_y,next_x) and normal_visited[next_y][next_x]==0 and data[next_y][next_x] == color:
            normal_visited[next_y][next_x] = True
            normal(next_y,next_x,data[next_y][next_x])

def abnormal(here_y,here_x,color):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    for dir in range(len(dy)):
        next_y = here_y + dy[dir]
        next_x = here_x + dx[dir]
        
        if IsSafe(next_y,next_x) and abnormal_visited[next_y][next_x]==0 and data[next_y][next_x] == color:
            abnormal_visited[next_y][next_x] = True
            abnormal(next_y,next_x,data[next_y][next_x])
        

N = int(input())
data = []
for rows in range(N):
    row = list(input())
    data.append(row)

normal_visited=[[0 for _ in range(N)] for _ in range(N)]
abnormal_visited=[[0 for _ in range(N)] for _ in range(N)]
cnt=0
res=0
ans=[]

for y in range(N):
    for x in range(N):
        if normal_visited[y][x] ==0:
            normal_visited[y][x] = True
            cnt+=1
            normal(y,x,data[y][x])
ans.append(cnt)

for i in range(N):
    for j in range(N):
        if data[i][j] == 'G':
            data[i][j] = 'R'


for y_idx in range(N):
    for x_idx in range(N):
        if abnormal_visited[y_idx][x_idx] ==0:
            abnormal_visited[y_idx][x_idx] = True
            res+=1
            abnormal(y_idx,x_idx,data[y_idx][x_idx])
ans.append(res)

print(*ans)