import sys
sys.stdin = open('어디에단어.txt','r')

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    data = []
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    count = 0
    # 가로검사
    for y in range(N):
        white_sum = 0
        white_found = False
        excess = False
        for x in range(N):
            if data[y][x] == 1:
                white_found = True

                if excess:
                    pass
                else:
                    white_sum += 1
                    if white_sum == M:
                        count+=1
                    elif white_sum > M:
                        excess=True
                        count-=1
                        white_sum=0
            elif data[y][x] == 0:
                if white_found:
                    excess=False
                    white_sum =0

    # 전치행렬
    for y in range(N):
        for x in range(N):
            if y>x:
                data[y][x], data[x][y] = data[x][y], data[y][x]

    # 세로검사

    for trans_y in range(N):
        trans_white_sum = 0
        trans_white_found = False
        trans_excess = False
        for trans_x in range(N):
            if data[trans_y][trans_x] == 1:
                trans_white_found = True
                if trans_excess:
                    pass
                else:
                    trans_white_sum+=1
                    if trans_white_sum == M:
                        count+=1
                    elif trans_white_sum > M:
                        trans_excess = True
                        count-=1
                        trans_white_sum =0
            elif data[trans_y][trans_x] == 0:
                if trans_white_found:
                    trans_excess = False
                    trans_white_sum =0
                else:
                    pass
    print('#{0} {1}'.format(time+1,count))