


MyMap=[[0]*8 for i in range(8)]
visited=[0]*8

def DFS(here):
    print(here)
    visited[here]=True

    for next in range(8):
        if MyMap[here][next] and not visited[next]:
            DFS(next)

# Data = list(map(int, input().split()))
Data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
howmany = int(len(Data)/2)

for i in range(howmany):
    start = Data[i*2]
    stop = Data[i*2+1]
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

DFS(1)

