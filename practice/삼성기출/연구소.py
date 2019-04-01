import sys
import copy
sys.stdin = open('연구소.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and y<N and x<M:
        return True

def bfs(y,x):
    global total
    Q.append(y)
    Q.append(x)
    visited[y][x]==True
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    while Q:
        here_y = Q.pop(0)
        here_x = Q.pop(0)
        for dir in range(len(dy)):
            next_y = here_y + dy[dir]
            next_x = here_x + dx[dir]
            if IsSafe(next_y,next_x) and data[next_y][next_x]==0 and visited[next_y][next_x]==0:
                visited[next_y][next_x] =True
                data[next_y][next_x] = 2
                Q.append(next_y)
                Q.append(next_x)
            elif IsSafe(next_y,next_x) and data[next_y][next_x]==1 and visited[next_y][next_x]==0:
                visited[next_y][next_x] = True

            elif IsSafe(next_y,next_x) and data[next_y][next_x]==2 and visited[next_y][next_x]==0:
                pass






T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    origin_data=[]

    for rows in range(N):
        row = list(map(int,input().split()))
        origin_data.append(row)
    data = copy.deepcopy(origin_data)
    max_cnt = 0

    for wall1_y in range(N):
        for wall1_x in range(M):
            if origin_data[wall1_y][wall1_x] == 0:
                for wall2_y in range(N):
                    for wall2_x in range(M):
                        # if origin_data[wall2_y][wall2_x]==0 and wall1_x!=wall2_x:
                            for wall3_y in range(N):
                                for wall3_x in range(M):
                                    # if origin_data[wall3_y][wall3_x]==0 and wall1_x!=wall3_x and wall2_x!=wall3_x:

                                        visited = [[0 for _ in range(M)] for _ in range(N)]
                                        data[wall1_y][wall1_x] = 1
                                        data[wall2_y][wall2_x] = 1
                                        data[wall3_y][wall3_x] = 1

                                        cnt=0
                                        for y in range(N):
                                            for x in range(M):
                                                if data[y][x] ==2 and visited[y][x]==0:
                                                    visited[y][x]=True
                                                    Q=[]
                                                    bfs(y,x)
                                        for safe_zone_y in range(N):
                                            for safe_zone_x in range(M):
                                                if data[safe_zone_y][safe_zone_x]==0:
                                                    cnt+=1
                                        if cnt > max_cnt:
                                            max_cnt = cnt
                                        data = copy.deepcopy(origin_data)

    print(max_cnt)