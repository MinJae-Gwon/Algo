import sys
sys.stdin = open('dfs_bfs.txt','r')

def dfs(deep,here):
    global dfs_res
    dfs_res.append(here)
    if deep == N:
        return
    for next_node in range(1,N+1):
        if data[here][next_node] ==1 and visited[next_node]==0:
            visited[next_node] = True
            dfs(deep+1,next_node)
            
def bfs(start):
    global bfs_res
    Q.append(start)
    bfs_visited[start] = True
    while Q:
        here=Q.pop(0)
        bfs_res.append(here)
        for next_node in range(1,N+1):
            if data[here][next_node]==1 and bfs_visited[next_node]==0:
                bfs_visited[next_node]=True
                Q.append(next_node)


N,M,V = map(int,input().split())
data=[[0 for _ in range(N+1)] for _ in range(N+1)]
for infos in range(M):
    y,x = map(int,input().split())
    data[y][x] = 1
    data[x][y] = 1

dfs_res=[]
visited = [0]*(N+1)
visited[V] = True
dfs(0,V)
print(*dfs_res)

bfs_res=[]
Q=[]
bfs_visited = [0]*(N+1)
bfs(V)
print(*bfs_res)


