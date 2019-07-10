import sys
sys.stdin = open('dice.txt','r')

def out(y,x):
    if x<0 or y<0 or x>=M or y>=N:
        return True

def south():
    dice[0], dice[1] = dice[1], dice[0]
    dice[1], dice[4] = dice[4], dice[1]
    dice[1], dice[5] = dice[5], dice[1]

    return

def north():
    dice[0], dice[1] = dice[1], dice[0]
    dice[4], dice[5] = dice[5], dice[4]
    dice[0], dice[5] = dice[5], dice[0]

    return

def west():
    dice[3], dice[5] = dice[5], dice[3]
    dice[0], dice[3] = dice[3], dice[0]
    dice[0], dice[2] = dice[2], dice[0]

    return

def east():
    dice[2], dice[5] = dice[5], dice[2]
    dice[0], dice[3] = dice[3], dice[0]
    dice[2], dice[3] = dice[3], dice[2]

    return

def go(y,x):
    for dir in directions:
        #north
        if dir == 3:
            new_x = x
            new_y = y-1
            if out(new_y,new_x):
                continue
            else:
                north()
                print(dice[0])
                if data[new_y][new_x] ==0:
                    data[new_y][new_x] = dice[-1]
                else:
                    dice[-1] = data[new_y][new_x]
                    data[new_y][new_x] = 0
        #east
        elif dir == 1:
            new_x = x+1
            new_y = y
            if out(new_y,new_x):
                continue
            else:
                east()
                print(dice[0])
                if data[new_y][new_x] ==0:
                    data[new_y][new_x] = dice[-1]
                else:
                    dice[-1] = data[new_y][new_x]
                    data[new_y][new_x] = 0
        #west
        elif dir == 2:
            new_x = x-1
            new_y = y
            if out(new_y,new_x):
                continue
            else:
                west()
                print(dice[0])
                if data[new_y][new_x] ==0:
                    data[new_y][new_x] = dice[-1]
                else:
                    dice[-1] = data[new_y][new_x]
                    data[new_y][new_x] = 0
        #south
        elif dir == 4:
            new_x = x
            new_y = y+1

            if out(new_y,new_x):
                continue
            else:
                south()
                # print(new_y,new_x)
                print(dice[0])
                if data[new_y][new_x] ==0:
                    data[new_y][new_x] = dice[-1]
                else:
                    dice[-1] = data[new_y][new_x]
                    data[new_y][new_x] = 0

        y = new_y
        x = new_x


N,M,X,Y,K = list(map(int,input().split()))
data=[[0 for _ in range(M)] for _ in range(N)]

for y in range(N):
    info = list(map(int,input().split()))
    for x in range(M):
        data[y][x] = info[x]

directions =list(map(int,input().split()))
dice=[0,0,0,0,0,0]
go(X,Y)