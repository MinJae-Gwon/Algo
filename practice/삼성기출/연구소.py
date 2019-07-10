import sys
import copy
sys.stdin = open('연구소.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and y<N and x<M:
        return True

def bfs(y,x):
    global Q,tempdata
    Q.append(y)
    Q.append(x)

    dy=[0,1,0,-1]
    dx=[1,0,-1,0]
    while Q:
        here_y = Q.pop(0)
        here_x = Q.pop(0)
        for dir in range(len(dy)):
            next_y = here_y + dy[dir]
            next_x = here_x + dx[dir]
            if IsSafe(next_y,next_x) and tempdata[next_y][next_x]==0:
                tempdata[next_y][next_x]=2

                Q.append(next_y)
                Q.append(next_x)

def wall(c,idx):
    global tempdata,Q, max_cnt
    if c==3:

        tempdata = copy.deepcopy(data)

        for wall_idx in range(3):
            y = temp[wall_idx] // M
            x = temp[wall_idx] % M
            if tempdata[y][x] ==2 or tempdata[y][x]==1:
                return
            elif tempdata[y][x]==0:
                tempdata[y][x]=1

        for y_idx in range(N):
            for x_idx in range(M):
                if tempdata[y_idx][x_idx]==2:
                    Q=[]
                    bfs(y_idx,x_idx)

        cnt=0
        for safe_y in range(N):
            for safe_x in range(M):
                if tempdata[safe_y][safe_x]==0:
                    cnt+=1

        if cnt > max_cnt:
            max_cnt = cnt

        return

    for i in range(idx,N*M):
        temp.append(i)
        wall(c+1,i+1)
        temp.pop()


N,M = map(int,input().split())
data=[]
for rows in range(N):
    row = list(map(int,input().split()))
    data.append(row)

#virus_loca
temp=[]
max_cnt = 0
wall(0,0)
print(max_cnt)