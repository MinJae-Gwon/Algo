import sys
sys.stdin = open("pin.txt","r")
def out(y,x):
    if y<0 or x<0 or y>=N or x>=N:
        return True

def poly_wall_hill(y,x,dir,poly):
    if poly==1 and dir==0 or poly==1 and dir==3 or poly==2 and dir==0 or poly==2 and dir==1 or poly==3 and dir==2 or poly==3 and dir==1 or poly==4 and dir==3 or poly==4 and dir==2 or poly==5:
        return 'bounce'
    else:
        return 'curve'

def curve_dir(dir,poly):
    if poly==1:
        if dir==1:
            return 3
        elif dir==2:
            return 1
    elif poly==2:
        if dir==2:
            return 3
        elif dir==3:
            return 1
    elif poly==3:
        if dir==3:
            return 3
        elif dir==0:
            return 1
    elif poly==4:
        if dir==0:
            return 3
        elif dir==1:
            return 1


def teleport(y,x,num):
    for row in range(N):
        for col in range(N):
            if (row!=y or col!=x) and data[row][col] == num:
                return (row,col)

def go(ball):
    global score
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    here_y = ball[0]
    here_x = ball[1]
    now_direction = ball[2]

    while True:
        # print(start_y,start_x,ball[2])
        # print(here_y,here_x)
        new_y = here_y + dy[now_direction]
        new_x = here_x + dx[now_direction]

        if out(new_y,new_x):
            score+=1
            now_direction = (now_direction+2)%4
            # here_y=new_y
            # here_x=new_x
        elif data[new_y][new_x] == -1:
            break


        elif 0< data[new_y][new_x] <6:

            what = poly_wall_hill(new_y,new_x,now_direction,data[new_y][new_x])
            if what=='bounce':
                # print('빠운스')
                # print(new_y,new_x)
                score+=1
                # print(now_direction)
                now_direction = (now_direction + 2) % 4
                # print(now_direction)
                # here_y = new_y
                # here_x = new_x
                # print('시작',start_y,start_x)
                # print('e다음',here_y,here_x)

            elif what=='curve':
                score+=1
                what = curve_dir(now_direction,data[new_y][new_x])
                now_direction = (now_direction + what)%4
                # here_y = new_y
                # here_x = new_x

        elif 5< data[new_y][new_x] < 11:
            hole = teleport(new_y,new_x,data[new_y][new_x])
            new_y = hole[0]
            new_x = hole[1]
        here_y = new_y
        here_x = new_x
        if new_y == start_y and new_x==start_x:
            break



T = int(input())
for time in range(T):
    N = int(input())
    data = []
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)
    # start_y = 0
    # start_x = 9
    # score = 0
    result  = 0
    for y in range(N):
        for x in range(N):
            for d in range(4):
                if data[y][x]==0:
                    start_y = y
                    start_x = x
                    score = 0
                    go([y,x,d])
                    if score>result:
                        result = score
    print('#{} {}'.format(time+1,result))