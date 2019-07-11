import sys
sys.stdin = open('길찾기.txt','r')

#swaea 1219번

def go(start):
    global cango

    if start == 99:
        cango = True
        return

    if sum(field[start]) == 0:
        return

    for i in range(100):
        if field[start][i] == 1:
            go(i)

for time in range(1,11):
    case_num, N = map(int,input().split())
    routes = list(map(int,input().split()))
    field = [[0 for _ in range(100)] for _ in range(100)]

    # 루트 표시
    for i in range(N):
        start_node = routes[2*i]
        end_node = routes[2*i+1]
        field[start_node][end_node] = 1

    cango = False
    go(0)

    if cango == True:
        print('#{0} {1}'.format(time, 1))
    else:
        print('#{0} {1}'.format(time,0))