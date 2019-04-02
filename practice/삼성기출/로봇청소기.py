import sys
sys.stdin = open('로봇청소기.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and x<M and y<N:
        return True
def dir_change(d):
    if d==0:
        return 3
    elif d==1:
        return 0
    elif d==2:
        return 1
    elif d==3:
        return 2

# d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽
def robot_go(here_y, here_x,direction):
    # dys = [[0,-1,0,1],[-1,0,1,0],[0,1,0,-1],[1,0,-1,0]]
    # dxs = [[-1,0,1,0],[0,1,0,-1],[1,0,-1,0],[0,-1,0,1]]
    #
    # dy = dys[direction]
    # dx = dxs[direction]
    #
    # for dir in range(len(dy)):
    #     next_y = here_y + dy[dir]
    #     next_x = here_x + dx[dir]
    #     next_direction = dir_change(direction)
    #     if dir==0 and IsSafe(next_y,next_x) and cleaned[next_y][next_x]==0:
    #         cleaned[next_y][next_x]=True
    #         robot_go(next_y,next_x,dir_change(direction))
    #     elif dir==0 and IsSafe(next_y,next_x) and cleaned[next_y][next_x]==True:
    #         robot_go(here_y,here_x,dir_change(direction))

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    r,c,d = map(int,input().split())
    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    cleaned = [[0 for _ in range(M)] for _ in range(N)]
    cleaned[r][c]=True
    robot_go(r,c,d)