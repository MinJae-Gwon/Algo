import sys

sys.stdin = open('ladder.txt','r')

for time in range(1):
    case_num = int(input())
    data = []
    for row_time in range(10):
        row = list(map(int,input().split()))
        data.append(row)

    for where_start in range(10):
        if data[9][where_start] == 2:
            start_x = where_start

    def Issafe(x):
        if x >= 0 and x < 10:
            return True

    dx=[-1,1,0]
    dy=[0,0,-1]
    start_y = 8
    point=0
    while True:
        for idx in range(point,len(dx)):
            new_start_y = start_y + dy[idx]
            new_start_x = start_x + dx[idx]
            if idx == 0 or idx == 1:
                if Issafe(new_start_x) and data[new_start_y][new_start_x] !=0:
                    if data[start_y-1][start_x] != 0 and start_y == new_start_y and start_x == new_start_x:
                        start_y = start_y -1
                        point =0
                    else:
                        start_x = new_start_x
                        start_y = new_start_y
                        point=0
            else:
                start_x = new_start_x
                start_y = new_start_y
                point=0

        if start_y ==0:
            break
    print(f'#{case_num} {start_x}')


