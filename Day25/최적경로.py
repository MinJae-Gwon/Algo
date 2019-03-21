# 삼성전자의 서비스 기사인 김대리는 회사에서 출발하여 냉장고 배달을 위해 N명의 고객을 방문하고 자신의 집에 돌아가려한다.
import sys
sys.stdin = open('최적경로.txt','r')

def pathfinder(here, sofar, deep):
    global min_path
    if sofar > min_path:
        return
    if deep==N:
        final = sofar+abs(here[0]-home[0])+abs(here[1]-home[1])
        if final < min_path:
            min_path = final
        return

    for next in range(N):
        if visited[next]==0:
            visited[next]=1
            pathfinder(data[next],sofar+abs(here[0]-data[next][0])+abs(here[1]-data[next][1]),deep+1)
            visited[next]=0

T = int(input())
for time in range(T):
    N = int(input())
    info = [ele for ele in map(int,input().split())]
    home = (info[0], info[1])
    company = (info[2], info[3])
    info=info[4:]

    data = []
    for i in range(len(info)//2):
        spot = (info[2*i], info[2*i+1])
        data.append((spot))

    visited = [0]*N
    min_path = 987654321
    pathfinder(company,0,0)
    print('#{0} {1}'.format(time+1,min_path))