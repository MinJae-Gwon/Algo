import sys
sys.stdin = open('그룹나누기.txt','r')

def bfs(start):
    global cnt
    Q.append(start)
    while Q:
        here = Q.pop(0)
        for next_node in range(1,N+1):
            if data[here][next_node] and visited[next_node] == 0:
                visited[next_node]=True
                Q.append(next_node)
    cnt+=1

T = int(input())
for time in range(T):
    N,M = map(int,input().split())

    data= [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0]*(N+1)
    node_infos = list(map(int,input().split()))
    for node in range(len(node_infos)//2):
        y = node_infos[2*node]
        x = node_infos[2*node+1]
        data[y][x] = 1
        data[x][y] = 1

    Q=[]
    cnt=0
    for start_node in range(1,N+1):
        if visited[start_node]==0:
            visited[start_node] = True
            bfs(start_node)

    print('#{0} {1}'.format(time+1,cnt))