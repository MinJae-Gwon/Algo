import sys
sys.stdin = open('미로02.txt','r')

def IsSafe(x,y):
    if x>=0 and y>=0 and x<100 and y<100:
        return True

def bfs(x,y):
    global canGo
    Q.append(x)
    Q.append(y)

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while Q:
        x = Q.pop(0)
        y = Q.pop(0)
        

        if x == 13 and y == 13:
            canGo = True
            break

        for dir in range(4):
            next_x = x + dx[dir]
            next_y = y + dy[dir]
            if IsSafe(next_x,next_y) and field[next_y][next_x] != 1 and visit[next_y][next_x] == 0:
                Q.append(next_x)
                Q.append(next_y)

for time in range(10):
    case = int(input())
    field = []
    for rows in range(100):
        row = list(map(int,input().split()))
        field.append(row)
    
    Q = []
    visit = [[0 for _ in range(100)] for _ in range(100)]
    visit[1][1] = True
    print(visit)
    canGo = False
    bfs(1,1)

    if canGo == True:
        print(1)
    else:
        print(0)