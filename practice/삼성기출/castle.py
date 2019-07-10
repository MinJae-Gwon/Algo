import sys
from copy import deepcopy
sys.stdin = open('castle','r')

def go(tmpfield):
    for y in range(N-1,-1,-1):
        for x in range(M-1,-1,-1):
            if y==N-1:
                tmpfield[y][x]=0
            elif tmpfield[y][x] ==1:
                tmpfield[y][x]=0
                tmpfield[y+1][x]=1


def shoot(tmpfield,tmpcount):
    while True:
        # for rw in tmpfield:
        #     print("qfff",rw)
        kill = []
        for a in range(M):
            if tmpfield[N][a] == 0:
                continue
            min_dist = 9876543321
            # print("a",a)
            min_y=-1;min_x=-1
            for x in range(M):
                for y in range(N):
                    if tmpfield[y][x] == 1:
                        dist = abs(y - N) + abs(x - a)
                        # print("dist",dist)
                        if dist <= D:
                            if dist < min_dist:
                                min_dist = dist
                                min_y = y
                                min_x = x
            # print("min",min_y,min_x)
            kill.append([min_y, min_x])
        for idx in range(len(kill)):
            if kill[idx][0] ==-1 or kill[idx][1]==-1:
                continue
            elif tmpfield[kill[idx][0]][kill[idx][1]] == 0:
                continue
            else:
                tmpfield[kill[idx][0]][kill[idx][1]] = 0
                tmpcount += 1
        go(tmpfield)
        enemy=0

        for y_idx in range(N):
            for x_idx in range(M):
                if tmpfield[y_idx][x_idx]==1:
                    enemy+=1
        if enemy == 0:
            return tmpcount


def attack(c,idx):
    global archer_row,kill_count
    if c==3:
        tmpcount=0
        for archer in range(len(archer_row)):
            if archer_row[archer] ==0:
                continue
            else:
                archer_row[archer] = [N, archer]
        tmpfield = deepcopy(field)
        tmpfield.append(archer_row)

        tmpresult =shoot(tmpfield,tmpcount)
        if tmpresult>kill_count:
            kill_count=tmpresult


        return

    for i in range(idx,M):
        archer_row[i] = 1
        attack(c+1,i+1)
        archer_row[i] = 0


N,M,D = map(int,input().split())
field = []
kill_count = 0
for rows in range(N):
    row = list(map(int,input().split()))
    field.append(row)

archer_row = [0]*M
attack(0,0)
print(kill_count)