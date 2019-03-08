import sys
sys.stdin = open('1215.회문1.txt','r')

for time in range(10):
    N = int(input())
    data =[]
    for rows in range(8):
        row = list(input())
        data.append(row)

    cnt = 0
    # 가로
    for y in range(8):
        for x in range(8-N+1):
            if data[y][x:x+N] == list(reversed(data[y][x:x+N])):
                cnt+=1

    for y_idx in range(8):
        for x_idx in range(8):
            if y_idx > x_idx:
                data[y_idx][x_idx], data[x_idx][y_idx] = data[x_idx][y_idx], data[y_idx][x_idx]

    # 세로
    for idx_y in range(8):
        for idx_x in range(8-N+1):
            if data[idx_y][idx_x:idx_x+N] == list(reversed(data[idx_y][idx_x:idx_x+N])):
                cnt+=1

    print('#{0} {1}'.format(time+1,cnt))