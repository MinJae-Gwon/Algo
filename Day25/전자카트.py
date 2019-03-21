#5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
import sys
sys.stdin = open('input.txt','r')


def pathfinder(here_y,deep,sofar):
    global min_elec
    if sofar >= min_elec:
        return 
    if deep==N and sum(visited) == N and here_y==0:
        if sofar < min_elec:
            min_elec = sofar
        return
    
    for next in range(N):
        if data[here_y][next] !=0 and visited[next] ==0:
            visited[next] = 1
            pathfinder(next,deep+1,sofar+data[here_y][next])
            visited[next] = 0

T = int(input())
for time in range(T):
    N = int(input())
    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)
    
    min_elec = 987654321
    visited =[0]*(N)

    pathfinder(0,0,0)
    print('#{0} {1}'.format(time+1,min_elec))

