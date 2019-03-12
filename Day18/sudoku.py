import sys
sys.stdin = open('sudoku.txt','r')

T = int(input())
for time in range(T):

    data=[]
    for rows in range(9):
        row = list(map(int,input().split()))
        data.append(row)


    no_sudoku_hori = False
    if not no_sudoku_hori:
        for y in range(9):
            check_hori=[]
            for x in range(9):
                if not check_hori:
                    check_hori.append(data[y][x])
                else:
                    if data[y][x] not in check_hori:
                        check_hori.append(data[y][x])
                    else:
                        no_sudoku_hori = True
                        break
            if no_sudoku_hori:
                break

    no_sudoku_verti = False
    if not no_sudoku_verti:
        for x_idx in range(9):
            check_verti = []
            for y_idx in range(9):
                if not check_verti:
                    check_verti.append(data[y_idx][x_idx])
                else:
                    if data[y_idx][x_idx] not in check_verti:
                        check_verti.append(data[y_idx][x_idx])
                    else:
                        no_sudoku_verti = True
                        break
            if no_sudoku_verti:
                break

    dx = [-1,0,1,-1,1,-1,0,1]
    dy =[-1,-1,-1,0,0,1,1,1]
    no_sudoku_square = False
    if not no_sudoku_square:
        for y_i in range(1,8,3):
            for x_i in range(1,8,3):
                check_square = []
                check_square.append(data[y_i][x_i])
                for dir in range(len(dx)):

                    if data[y_i+dy[dir]][x_i+dx[dir]] not in check_square:
                        check_square.append(data[y_i+dy[dir]][x_i+dx[dir]])
                    else:
                        no_sudoku_square = True
                        break
            if no_sudoku_square:
                break

    if no_sudoku_hori or no_sudoku_verti or no_sudoku_square:
        print('#{0} 0'.format(time + 1))
    elif not no_sudoku_hori and not no_sudoku_verti and not no_sudoku_square:
        print('#{0} 1'.format(time + 1))

