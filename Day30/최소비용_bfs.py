import sys
sys.stdin = open('최소비용.txt','r')

def IsSafe(y,x):
    if y>=0 and y<N and x>=0 and x<N:
        return True

def bfs(info):
    Q.append(info)
    dy=[0,1,0,-1]
    dx=[1,0,-1,0]
    while Q:
        here_info = Q.pop(0)
        for dir in range(len(dy)):
            next_y = here_info[0] + dy[dir]
            next_x = here_info[1] + dx[dir]
            if IsSafe(next_y,next_x):


T = int(input())
for time in range(T):
    N = int(input())
    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    mymap = [[987654321999 for _ in range(N)] for _ in range(N)]
    mymap[0][0] = data[0][0]
    Q=[]
    bfs((0,0,0))
    #(here_y,here_x,sofar)
    print('#{0} {1}'.format(time+1,mymap[N-1][N-1]))