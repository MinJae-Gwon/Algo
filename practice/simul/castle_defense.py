import sys
import copy
sys.stdin = open('castle.txt', 'r')

def over():
    global tmp_yard

    if len(tmp_yard)==0:
        return True

    total = 0
    for y in range(len(tmp_yard)):
        for x in range(M):
            if tmp_yard[y][x]==1:
                total+=1

    if total ==0:
        return True


def move():
    global tmp_yard

    tmp_yard.pop()
    print('gg',tmp_yard)


def shoot(y,x):
    global kill, tmp_yard

    if tmp_yard[y][x]==1:
        kill+=1
        tmp_yard[y][x]=0

    print('shoot',tmp_yard)

def detect(archer_x):
    global tmp_yard
    print('ppop')

    min_dist = 987654321
    min_y = 1000
    min_x = 1000
    for x in range(M):
        for y in range(len(tmp_yard)):
            if tmp_yard[y][x]==1:
                dist = abs(x-archer_x) + abs(y-len(tmp_yard))
                if dist>D:
                    continue
                elif dist<min_dist:
                    min_dist = dist
                    min_x = x
                    min_y = y
    print(min_y, min_x)
    return (min_y, min_x)


def go(c,idx):
    global tmp_yard, max_kill, kill
    if c==3:
        tmp_yard = copy.deepcopy(yard)
        archer_row = copy.deepcopy(visited)
        print('궁수', archer_row)

        kill=0
        while True:
            for archer_x in range(M):
                if archer_row[archer_x]==1:
                    enemy_y,enemy_x = detect(archer_x)
                    if enemy_y != 1000 and enemy_x != 1000:
                        shoot(enemy_y, enemy_x)

            move()

            if over():
                break
        print('kill',kill)
        if kill > max_kill:
            max_kill = kill
        return

    for i in range(idx,M):
        visited[i] = 1
        go(c+1,i+1)
        visited[i] = 0

N,M,D = map(int,input().split())
yard=[]
for rows in range(N):
    row = list(map(int,input().split()))
    yard.append(row)

#archer deploy
visited = [0]*M
max_kill=0
go(0,0)
print(max_kill)