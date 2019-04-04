import sys
sys.stdin = open('2048.txt','r')

def rotate(data):
    mymap = [[0 for _ in range(N)] for _ in range(N)]

    for y in range(N):
        for x in range(N):
            mymap[y][x] = data[x][N-1-y]

    return mymap

def push_left():
    new_map = []
    for y in range(N):
        i = 0
        new_row = []
        while True:
            if i > N-1:
                break
            elif i == N - 1:
                if data[y][i] != 0:
                    new_row.append(data[y][i])
                    break
                else:
                    break

            elif data[y][i] != 0 and data[y][i + 1] != 0 and data[y][i] == data[y][i + 1]:
                new_row.append(2 * data[y][i])
                i += 2

            elif data[y][i] != 0 and data[y][i + 1] == 0:
                data[y][i], data[y][i + 1] = data[y][i + 1], data[y][i]
                i += 1

            elif data[y][i] != 0 and data[y][i + 1] != 0 and data[y][i] != data[y][i + 1]:
                new_row.append(data[y][i])
                i += 1

            elif data[y][i] == 0:
                i += 1

        while len(new_row) < N:
            new_row = new_row + [0]

        new_map.append(new_row)
    return new_map

T=int(input())
for time in range(T):
    N, dir = map(str,input().split())
    N = int(N)

    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    if dir == 'left':
        res = push_left()
        print('#{0}'.format(time + 1))
        for r in range(N):
            print(*res[r])

    elif dir == 'right':
        data = rotate(data)
        data = rotate(data)
        res = push_left()
        res = rotate(res)
        res = rotate(res)
        print('#{0}'.format(time + 1))
        for r in range(N):
            print(*res[r])

    elif dir == 'up':
        data = rotate(data)
        res = push_left()
        res = rotate(res)
        res = rotate(res)
        res = rotate(res)
        print('#{0}'.format(time + 1))
        for r in range(N):
            print(*res[r])

    elif dir == 'down':
        data = rotate(data)
        data = rotate(data)
        data = rotate(data)
        res = push_left()
        res = rotate(res)
        print('#{0}'.format(time+1))
        for r in range(N):
            print(*res[r])
