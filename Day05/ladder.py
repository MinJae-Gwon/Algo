import sys

sys.stdin = open('ladder.txt','r')

for time in range(10):
    case_num = int(input())
    data = []
    for row_time in range(100):
        row = list(map(int,input().split()))
        data.append(row)

    for where_start in range(100):
        if data[99][where_start] == 2:
            start_x = where_start

    def Issafe(x,y):
        if x >= 0 and x < 100:
            return True
    def Ispass(x,y):
        if data[y][x] != 0:
            return True

    def Notvisited(x,y):
        if data[y][x] != 2:
            return True
    start_y = 98
    data[start_y][start_x] = 2

    dx=[-1,1,0]
    dy=[0,0,-1]

    while True:

        for i in range(len(dx)):
            new_start_x = start_x + dx[i]
            new_start_y = start_y + dy[i]

            if Issafe(new_start_x,new_start_y) and Ispass(new_start_x,new_start_y) and Notvisited(new_start_x, new_start_y):
                start_x = new_start_x
                start_y = new_start_y
                data[start_y][start_x] = 2
                break
            else:
                pass

        if start_y == 0:
            break


    print(f'#{case_num} {start_x}')


