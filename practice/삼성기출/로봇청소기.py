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

def dead_lock(y,x):
    global dy,dx
    for dir in range(4):
        next_y = y + dy[dir]
        next_x = x + dx[dir]
        if IsSafe(next_y,next_x):
            if cleaned[next_y][next_x]==True or data[next_y][next_x]==1:
                dead = True
                continue
            elif data[next_y][next_x]==0 and cleaned[next_y][next_x]==0:
                dead = False
                break

    if dead == True and data[y+dy[3]][x+dx[3]]==1:
        return True
    elif dead == False:
        return False

def bback(y,x):
    global dy, dx
    for dir in range(4):
        next_y = y + dy[dir]
        next_x = x + dx[dir]
        if IsSafe(next_y, next_x):
            if cleaned[next_y][next_x] == True or data[next_y][next_x] == 1:
                dead = True
                continue
            elif data[next_y][next_x] == 0 and cleaned[next_y][next_x] == 0:
                dead = False
                break

    if dead == True and data[y + dy[3]][x + dx[3]] == 0:
        return True
    elif dead == False:
        return False



# d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽
def robot_go(here_y, here_x,direction):
    global dy,dx
    dys = [[0,-1,0,1],[-1,0,1,0],[0,1,0,-1],[1,0,-1,0]]
    dxs = [[-1,0,1,0],[0,1,0,-1],[1,0,-1,0],[0,-1,0,1]]



    cnt=1
    while True:
        dy = dys[direction]
        dx = dxs[direction]

        if dead_lock(here_y,here_x):
            break

        if bback(here_y,here_x):
            here_y = here_y + dy[3]
            here_x = here_x + dx[3]
            continue
        if IsSafe(here_y+dy[0],here_x+dx[0]):
            if data[here_y+dy[0]][here_x+dx[0]] == 0 and cleaned[here_y+dy[0]][here_x+dx[0]]==0:
                cnt += 1
                here_y = here_y + dy[0]
                here_x = here_x + dx[0]
                direction = dir_change(direction)
                cleaned[here_y][here_x]=True
                continue

        if IsSafe(here_y+dy[0],here_x+dx[0]):
            if (data[here_y+dy[0]][here_x+dx[0]] == 0 and cleaned[here_y+dy[0]][here_x+dx[0]]==True) or data[here_y+dy[0]][here_x+dx[0]]==1:
                direction = dir_change(direction)

    return cnt

        # clean_done = False
        # for dir in range(len(dy)):
        #     next_y = here_y + dy[dir]
        #     next_x = here_x + dx[dir]
        #     next_direction = dir_change(direction)
        #     if IsSafe(next_y,next_x):
        #         if dir==0  and data[next_y][next_x]==0 and cleaned[next_y][next_x]==0:
        #             clean_done = True
        #             cleaned[next_y][next_x] = True
        #             direction = dir_change(direction)
        #             here_x = here_x -1
        #             continue
        #
        #         if data[next_y][next_x]==0 and cleaned[next_y][next_x]==0:
        #             continue
        #
        #         l=[]
        #         if clean_done == False and (data[next_y][next_x] ==1 or cleaned[next_y][next_x]==True):




    #             cleaned[next_y][next_x]=True
    #         robot_go(next_y,next_x,dir_change(direction))
    #     elif dir==0 and IsSafe(next_y,next_x) and cleaned[next_y][next_x]==True:
    #         robot_go(here_y,here_x,dir_change(direction))

N,M = map(int,input().split())
r,c,d = map(int,input().split())
data=[]
for rows in range(N):
    row = list(map(int,input().split()))
    data.append(row)

cleaned = [[0 for _ in range(M)] for _ in range(N)]
cleaned[r][c]=True
print(robot_go(r,c,d))