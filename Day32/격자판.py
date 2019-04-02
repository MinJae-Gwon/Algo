import sys
sys.stdin = open('격자판.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and x<4 and y<4:
        return True

def pathfinder(here_y,here_x,deep,sofar):
    global res
    if deep==6 and len(sofar)==7:
        if sofar not in res:
            res.append(sofar)
        return
    dy=[0,1,0,-1]
    dx=[1,0,-1,0]

    for dir in range(len(dy)):
        next_y = here_y + dy[dir]
        next_x = here_x + dx[dir]
        if IsSafe(next_y,next_x):
            pathfinder(next_y,next_x,deep+1,sofar+data[next_y][next_x])

T = int(input())
for time in range(T):
    data=[]
    for rows in range(4):
        row = list(map(str,input().split()))
        data.append(row)
    res=[]

    for y in range(4):
        for x in range(4):
            pathfinder(y,x,0,data[y][x])

    print('#{0} {1}'.format(time+1,len(res)))