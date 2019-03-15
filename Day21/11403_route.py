import sys
sys.stdin = open('route.txt','r')

def dfs(here):
    for i in range(1,N+1):
        if data[here][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(i)

N, M = map(int,input().split())
data= [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0

for infos in range(M):
    node1, node2 = map(int,input().split())
    data[node1][node2] = 1
    data[node2][node1] = 1

for i in range(1,N+1):
    if not visited[i]:
        visited[i]=1
        cnt+=1
        dfs(i)
print(cnt)
