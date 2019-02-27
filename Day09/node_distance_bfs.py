import sys
sys.stdin = open('node_distance_bfs.txt','r')

def Visited(a):
    if visited[a]:
        return True
def Getdistance(v):
    Q.append(v)
    visited[v] = True
    while Q:
        here = Q.pop(0)
        for next in range(len(data[here])):
            if data[here][next] ==1 and not Visited(next):
                Q.append(next)
                visited[next] = True
                distance[next] = distance[here] +1


T = int(input())
for time in range(T):
    # v = 노도 개수 / e = 간선 개수
    V,E = map(int,input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for connect in range(E):
        from_node, to_node = map(int,input().split())
        data[from_node][to_node] = 1
        data[to_node][from_node] = 1
    S,G = map(int,input().split())
    Q=[]
    visited = [0]*(V+1)
    distance = [0]*(V+1)
    Getdistance(S)
    print(f'#{time+1} {distance[G]}')
