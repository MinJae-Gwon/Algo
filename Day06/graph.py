import sys

sys.stdin = open('graph.txt','r')

#function
ans = 0
def pathfinder(here,to):
    global ans
    visited[here] = True
    if ans ==1:
        return

    if here == to:
        ans+=1
        return

    for next in range(len(visited)):
        if mymap[here][next]==1 and not visited[next]:
            pathfinder(next,to)

T=int(input())

for time in range(T):
    V, E = map(int,input().split())
    data = []
    for e in range(E):
        node1, node2 = map(int,input().split())
        data.append(node1)
        data.append(node2)
    S, G = map(int,input().split())
    # map에 경로 표시
    mymap = [[0 for _ in range(max(data)+1)] for _ in range(max(data)+1)]
    for i in range(0,len(data),2):
        start = i
        end = i+1
        mymap[data[start]][data[end]] = 1

    # visited 생성
    visited = [0]*(max(data)+1)



    pathfinder(S,G)
    print(f'#{time+1} {ans}')
    ans=0


