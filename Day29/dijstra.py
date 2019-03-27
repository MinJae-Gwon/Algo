import sys
sys.stdin = open('dijstra.txt','r')

T = int(input())
for time in range(T):
    N,M,start_node = map(int,input().split())

    data=[[987654321 for _ in range(N)] for _ in range(N)]
    for connects in range(M):
        y,x,weight = map(int,input().split())
        data[y][x] = weight

    dist = [987654321]*(N)
    dist[start_node] = 0

    T = [ele for ele in range(N)]
    S = []

    while T:
        v = min(T)
        v_idx = T.index(v)
        T_out = T.pop(v_idx)
        S.append(T_out)

        for w in range(N):
            dist[w] = min(dist[w],dist[v]+data[v][w])
    print(dist)


