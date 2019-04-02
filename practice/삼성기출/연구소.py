import sys
import copy
sys.stdin = open('연구소.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and y<N and x<M:
        return True

def bfs(y,x):
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
            if IsSafe(next_y,next_x) and data[next_y][next_x]==0 and visited[next_y][next_x]==0:
                visited[next_y][next_x]=True

                Q.append(next_y)
                Q.append(next_x)

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    #virus_loca
    virus_loca=[]
    for v_y in range(N):
        for v_x in range(M):
            if data[v_y][v_x]==2:
                v_loca = (v_y,v_x)
                virus_loca.append(v_loca)

    wall1 = []
    for i in range(N):
        for j in range(M):
            loca = (i,j)
            wall1.append(loca)
    wall2=[]
    for i in range(N):
        for j in range(M):
            loca = (i,j)
            wall2.append(loca)
    wall3=[]
    for i in range(N):
        for j in range(M):
            loca = (i,j)
            wall3.append(loca)

    max_cnt=0
    for w1 in wall1:
        y1,x1=w1
        if data[y1][x1]==0:
            for w2 in wall2:
                y2,x2=w2
                if data[y2][x2] == 0 and w1!=w2:
                    for w3 in wall3:
                        y3,x3=w3
                        if data[y3][x3] == 0 and w3!=w2 and w3!=w1:
                            data[y1][x1]=1
                            data[y2][x2]=1
                            data[y3][x3]=1
                            for virus in range(len(virus_loca)):
                                Q=[]
                                visited = [[0 for _ in range(M)] for _ in range(N)]
                                gz_y, gz_x = virus_loca[virus]
                                bfs(gz_y, gz_x)
                            cnt=0
                            for check_y in range(N):
                                for check_x in range(M):
                                    if data[check_y][check_x]==0 and visited[check_y][check_x]==0:
                                        cnt+=1

                            if cnt>max_cnt:
                                max_cnt=cnt

                            data[y1][x1] = 0
                            data[y2][x2] = 0
                            data[y3][x3] = 0


    print(max_cnt)