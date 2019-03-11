import sys
sys.stdin = open('1996_apartment.txt','r')

def NotVisited(y,x):
    if visited[y][x] ==0:
        return True
def IsSafe(y,x):
    if x >= 0 and x < N and y >=0 and y < N:
        return True
def IsPossible(y,x):
    if data[y][x] !=0:
        return True


def bfs(here_y, here_x):
    global Q, apart_cnt, hood_cnt, apart_cnt_list
    visited[here_y][here_x] =True
    Q.append(here_y)
    Q.append(here_x)
    apart_cnt+=1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while Q:
        start_y = Q.pop(0)
        start_x = Q.pop(0)
        for dir in range(len(dx)):
            next_y = start_y + dy[dir]
            next_x = start_x + dx[dir]
            if IsSafe(next_y,next_x) and IsPossible(next_y, next_x) and NotVisited(next_y, next_x):
                visited[next_y][next_x] = True
                Q.append(next_y)
                Q.append(next_x)
                apart_cnt+=1
    apart_cnt_list.append(apart_cnt)
    apart_cnt=0
    hood_cnt+=1



N = int(input())
data=[]
for rows in range(N):
    row = [int(comp) for comp in list(input())]
    data.append(row)

visited = [[0 for _ in range(N)] for _ in range(N)]
Q=[]
apart_cnt_list =[]
apart_cnt = 0
hood_cnt =0

for y in range(N):
    for x in range(N):
        if data[y][x] !=0 and NotVisited(y,x):
            bfs(y,x)

apart_cnt_list = sorted(apart_cnt_list)
print(hood_cnt)

for ele in apart_cnt_list:
    print(ele)