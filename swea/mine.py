import sys
sys.stdin = open('mine.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and x<N and y<N:
        return True

def mine_check(y,x):
    mine_count = 0
    for dir in range(8):
        n_y = y + dy[dir]
        n_x = x + dx[dir]

        if IsSafe(n_y,n_x) and field[n_y][n_x] == '*':
            mine_count += 1
    return mine_count

def blow(y,x):

    total_mine = mine_check(y,x)
    if total_mine > 0:
        field[y][x] = total_mine

    else:
        field[y][x] = 0

        for dir in range(8):
            n_y = y + dy[dir]
            n_x = x + dx[dir]

            if IsSafe(n_y,n_x) and field[n_y][n_x] == '.':
                blow(n_y,n_x)


T = int(input())
for time in range(T):
    N = int(input())

    field = []
    for rows in range(N):
        row = list(input())
        field.append(row)

    # print(field)
    dy = [-1,-1,0,1,1,1,0,-1]
    dx = [0,1,1,1,0,-1,-1,-1]

    total_click = 0
    for y in range(N):
        for x in range(N):
            if field[y][x] == '.' and mine_check(y,x) == 0:
                blow(y,x)
                total_click += 1

    for i in range(N):
        for j in range(N):
            if field[i][j] == '.':
                blow(y,x)
                total_click += 1

    print('#{0} {1}'.format(time+1,total_click))
