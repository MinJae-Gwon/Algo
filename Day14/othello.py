import sys
sys.stdin = open('othello.txt','r')

def Out(x,y):
    if x<0 or x>N-1 or y<0 or y>N-1:
        return True

T = int(input())
for time in range(T):
    N , M = map(int,input().split())
    data = [[0 for _ in range(N) ]for _ in range(N)]

    data[N//2-1][N//2-1] = 2
    data[N//2-1][N//2] = 1
    data[N//2][N//2-1] = 1
    data[N//2][N//2] = 2

    put_info = []
    for positions in range(M):
        position = list(map(int,input().split()))
        put_info.append(position)


    for turn in range(M):
        x = put_info[turn][0]-1
        y = put_info[turn][1]-1
        here_x = x
        here_y = y
        stone = put_info[turn][2]
        data[y][x] = stone

        dx = [-1,1,0,0,-1,1,-1,1]
        dy = [0,0,-1,1,-1,-1,1,1]

        for dir in range(len(dx)):
            stone_found = False
            while True:
                new_x = here_x + dx[dir]
                new_y = here_y + dy[dir]
                if Out(new_x,new_y) or data[new_y][new_x] == 0:
                    break
                if data[new_y][new_x] == stone:
                    stone_found = True
                    break
                here_x = new_x
                here_y = new_y

            if stone_found:
                while True:
                    back_x = new_x - dx[dir]
                    back_y = new_y - dy[dir]
                    data[back_y][back_x] = stone
                    if back_x == x and back_y == y:
                        break
                    new_x = back_x
                    new_y = back_y
            here_x = x
            here_y = y

    white = 0
    black = 0
    for y_idx in range(N):
        for x_idx in range(N):
            if data[y_idx][x_idx] == 1:
                black+=1
            elif data[y_idx][x_idx] == 2:
                white+=1
    print('#{0} {1} {2}'.format(time+1,black,white))