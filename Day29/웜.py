import sys
sys.stdin = open('웜.txt','r')

def dfs(here):
    if sum(data[here])==0:
        return
    for next_node in range(1,N+1):
        if data[here][next_node]==1 and visited[next_node]==0:
            visited[next_node]=True
            res[next_node]=1
            dfs(next_node)

N = int(input())
M = int(input())
data=[[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0]*(N+1)
res=[0]*(N+1)

for connects in range(M):
    y,x = map(int,input().split())
    data[y][x] = 1
    data[x][y] = 1

dfs(1)
print(sum(res)-1)
