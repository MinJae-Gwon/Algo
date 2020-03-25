import sys
sys.stdin = open('파이프옮기기.txt','r')


def IsSafe(y,x):
    if y>=0 and x>=0 and y<N and x<N and field[y][x] == 0:
        return True

# stat -> 0:가로, 1:세로, 2: 대각
def go(y,x,stat):
    global cnt

    if y == N-1 and x == N-1:
        cnt += 1
        return

    if stat == 0:
        if IsSafe(y,x+1):
            if field[y][x+1] == 0:
                go(y,x+1,0)
        if IsSafe(y+1,x+1):
            if field[y][x+1] == 0 and field[y+1][x+1] == 0 and field[y+1][x] == 0:
                go(y+1,x+1,2)
    elif stat == 1:
        if IsSafe(y+1,x):
            if field[y+1][x] == 0:
                go(y+1,x,1)
        if IsSafe(y+1,x+1):
            if field[y][x + 1] == 0 and field[y + 1][x + 1] == 0 and field[y + 1][x] == 0:
                go(y + 1, x + 1, 2)

    else:
        if IsSafe(y,x+1):
            if field[y][x+1] == 0:
                go(y,x+1,0)
        if IsSafe(y+1,x):
            if field[y+1][x] == 0:
                go(y+1,x,1)
        if IsSafe(y+1,x+1):
            if field[y][x+1] == 0 and field[y+1][x+1] == 0 and field[y+1][x] == 0:
                go(y+1,x+1,2)



N = int(input())
field = []

for rows in range(N):
    row = list(map(int,input().split()))
    field.append(row)

cnt = 0
go(0,1,0)

print(cnt)