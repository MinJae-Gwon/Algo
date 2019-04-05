import sys
sys.stdin = open('오델로.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and x<N and y<N:
        return True


def get_stone(info):
    y = info[0]
    x = info[1]
    stone = info[2]

    data[y][x] = stone

    dy=[-1,-1,0,1,1,1,0,-1]
    dx=[0,1,1,1,0,-1,-1,-1]

    for dir in range(8):
        n_y = y + dy[dir]
        n_x = x + dx[dir]
        if IsSafe(n_y,n_x) and data[n_y][n_x]!=0 and data[y][x]!=data[n_y][n_x]:
            same=1
            while True:
                n_y = n_y + dy[dir]
                n_x = n_x + dx[dir]
                if not IsSafe(n_y,n_x):
                    break
                if data[y][x] == data[n_y][n_x]:
                    while True:
                        if same ==0:
                            break
                        n_y = n_y - dy[dir]
                        n_x = n_x - dx[dir]

                        data[n_y][n_x] = stone

                        same-=1

                if data[y][x] != data[n_y][n_x]:
                    same+=1




T = int(input())
for time in range(T):
    N,M = map(int,input().split())

    data = [[0 for _ in range(N)] for _ in range(N)]
    # black_stone = 1, white_stone = 2
    data[N//2-1][N//2] = 1
    data[N//2][N//2-1] = 1
    data[N//2-1][N//2-1] = 2
    data[N//2][N//2] = 2
    print(data)
    info = []
    for infos in range(M):
        y,x,stone = map(int,input().split())
        y -=1
        x -=1
        info.append((y,x,stone))

    for put_stone in info:
        get_stone(put_stone)

    black_stone =0
    white_stone =0
    for y_idx in range(N):
        for x_idx in range(N):
            if data[y_idx][x_idx]==1:
                black_stone+=1
            elif data[y_idx][x_idx]==2:
                white_stone+=1

    print('#{0} {1} {2}'.format(time+1, black_stone, white_stone))
