#마이구미 Problem box_20
import sys
sys.stdin = open('보급로.txt','r')

def IsSafe(y,x):
    if y>=0 and y<N and x>=0 and x<N:
        return True
def NotVisited(y,x):
    if visited[y][x] == 0:
        return True

def pathfinder(here_y, here_x,sofar):
    global min_path
    if sofar >= min_path:
        return
    if here_y == N-1 and here_x == N-1:
        if sofar < min_path:
            min_path = sofar
        return

    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    for dir in range(len(dy)):
        next_y = here_y + dy[dir]
        next_x = here_x + dx[dir]
        if IsSafe(next_y,next_x) and NotVisited(next_y,next_x) and sofar<map[next_y][next_x]:
            visited[next_y][next_x] = True
            map[next_y][next_x]= sofar
            pathfinder(next_y,next_x,sofar+data[next_y][next_x])
            visited[next_y][next_x] = 0

T = int(input())
for time in range(T):
    N = int(input())
    min_path = 987654321
    visited = [[0 for _ in range(N)] for _ in range(N)]
    map = [[987654321 for _ in range(N)] for _ in range(N)]
    data=[]
    for rows in range(N):
        row = [int(ele) for ele in list(input())]
        data.append(row)

    pathfinder(0,0,0)
    print('#{0} {1}'.format(time+1,min_path))