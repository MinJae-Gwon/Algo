import sys
sys.stdin = open('케빈베이컨.txt','r')

def kevin_bacon(here,to,sofar):
    global min_route
    if sofar > min_route:
        return
    if here==to:
        if sofar < min_route:
            min_route = sofar
        return
    for next_node in range(1,N+1):
        if data[here][next_node] ==1 and visited[next_node] == 0:
            visited[next_node] = True
            kevin_bacon(next_node,to,sofar+1)
            visited[next_node] = 0


N,M = map(int,input().split())
data=[[0 for _ in range(N+1)] for _ in range(N+1)]
for infos in range(M):
    y,x = map(int,input().split())
    data[y][x] = 1
    data[x][y] = 1


ans=[]
for start in range(1,N+1):
    res=0
    for destination in range(1,N+1):
        visited = [0] * (N + 1)
        if start!=destination:
            min_route = 987654321
            visited[start] = True
            kevin_bacon(start,destination,0)
            res+=min_route
            visited[start] = 0
    ans.append(res)

min_user = ans.index(min(ans))
print(min_user+1)
