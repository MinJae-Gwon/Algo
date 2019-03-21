#5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
import sys
sys.stdin = open('최소합.txt','r')

def IsSafe(y,x):
    if x>=0 and x<N and y>=0 and y<N:
        return True

def pathfinder(here_y, here_x, sofar):
    global min_sum
    if sofar > min_sum:
        return
    if here_y == N-1 and here_x == N-1:
        if sofar < min_sum:
            min_sum = sofar
        return
    
    dy = [0,1]
    dx = [1,0]

    for dir in range(len(dy)):
        next_y = here_y + dy[dir]
        next_x = here_x + dx[dir]
        if IsSafe(next_y, next_x) and visited[next_y][next_x] ==0:
            visited[next_y][next_x] =True
            pathfinder(next_y,next_x,sofar+data[next_y][next_x])
            visited[next_y][next_x] = 0




T = int(input())
for time in range(T):
    N = int(input())
    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    visited=[[0 for _ in range(N)] for _ in range(N)]
    min_sum = 987654321

    pathfinder(0,0,data[0][0])
    print('#{0} {1}'.format(time+1,min_sum))