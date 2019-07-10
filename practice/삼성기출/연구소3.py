import sys
import copy
sys.stdin = open('연구소3.txt','r')

def short_path():
    global tmpmap
    max_path = 0
    for i in range(N):
        for j in range(N):
            # if tmpmap[i][j] != 'active' or tmpmap[i][j] != '*' or tmpmap[i][j] != '-':
            if IsSafe(i,j):
                if tmpmap[i][j] > max_path:
                    max_path = tmpmap[i][j]
    return max_path

def cango(y,x,dis):
    global tmpmap
    if tmpmap[y][x]==0 or tmpmap[y][x] > dis:
        return True

def IsSafe(y,x):
    global tmpmap
    if y>=0 and x>=0 and y<N and x<N and tmpmap[y][x] != '-' and tmpmap[y][x] != '*' and tmpmap[y][x] != 'active':
        return True

def bfs(info):
    global Q, tmpmap, visited
    y = info[0]
    x = info[1]
    sofar = info[2]

    Q.append(y)
    Q.append(x)
    Q.append(sofar)

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    while Q:
        now_y = Q.pop(0)
        now_x = Q.pop(0)
        now_sofar = Q.pop(0)

        for dir in range(4):
            next_y = now_y + dy[dir]
            next_x = now_x + dx[dir]
            next_sofar = now_sofar + 1
            if IsSafe(next_y, next_x) and visited[next_y][next_x] == 0 and cango(next_y, next_x, next_sofar):
                visited[next_y][next_x] = True
                tmpmap[next_y][next_x] = next_sofar
                Q.append(next_y)
                Q.append(next_x)
                Q.append(next_sofar)


def go(c,idx):
    global Q, tmpmap, visited, min_res
    if c==M:
        # print(picked)
        # print(virus)
        tmpmap = copy.deepcopy(data)
        # print(tmpmap)
        # 활성 바이러스 표시
        active_virus = []
        for v in range(len(picked)):
            if picked[v]==1:
                virus_block = virus[v]
                # print(virus_block)
                active_virus_y = virus_block//N
                active_virus_x = virus_block%N
                # print(virus_y,virus_x)
                tmpmap[active_virus_y][active_virus_x]='active'
                active_virus_info = [active_virus_y,active_virus_x,0]
                active_virus.append(active_virus_info)
        # print(tmpmap)
        #비활성 바이러스 표시
        for i in range(N):
            for j in range(N):
                if tmpmap[i][j]==2:
                    tmpmap[i][j]='*'
        # print(tmpmap)

        for info in active_virus:
            # print(info)
            Q=[]
            visited = [[0 for _ in range(N)] for _ in range(N)]
            bfs(info)
        print(tmpmap)

        how_far = short_path()
        if min_res > how_far:
            min_res = how_far


        return

    for i in range(idx, len(virus)):
        picked[i] = 1
        go(c+1, i+1)
        picked[i] = 0


N, M = map(int,input().split())
data = []
for rows in range(N):
    row = list(map(int,input().split()))
    data.append(row)

virus = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            data[i][j] = '-'

        elif data[i][j] == 2:
            virus.append(N*i+j)
print(virus)

min_res = 987754329
picked = [0]*len(virus)
go(0,0)
print(min_res)