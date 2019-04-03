import sys
sys.stdin = open('정사각형방.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and x<N and y<N:
        return True

def bfs(info):
    global cnt
    Q.append(info)

    dy=[0,1,0,-1]
    dx=[1,0,-1,0]
    while Q:
        here_info = Q.pop(0)
        here_y = here_info[0]
        here_x = here_info[1]

        for dir in range(len(dy)):
            next_y = here_y + dy[dir]
            next_x = here_x + dx[dir]
            if IsSafe(next_y,next_x) and data[here_y][here_x]+1 == data[next_y][next_x]:
                cnt+=1
                next_info = (next_y,next_x)
                Q.append(next_info)


T = int(input())
for time in range(T):
    N = int(input())
    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    mymap=[[0 for _ in range(N)] for _ in range(N)]

    max_cnt=1
    for y in range(N):
        for x in range(N):
            Q=[]
            cnt=1
            bfs((y,x))

            mymap[y][x] = cnt
            if cnt > max_cnt:
                max_cnt = cnt

    min_room = 999999999999999999999999999999999999999999999999999999999999999999999999999999
    for n in range(N):
        for m in range(N):
            if mymap[n][m] == max_cnt:
                if data[n][m] < min_room:
                    min_room = data[n][m]


    print('#{0} {1} {2}'.format(time+1, min_room, max_cnt))