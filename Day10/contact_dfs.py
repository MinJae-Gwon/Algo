import sys
sys.stdin = open('contact_dfs.txt','r')

def NotVistied(a):
    if visited[a] == 0:
        return True

def dfs(here):
    global distance, visited
    visited[here] = True
    if not data[here]:
        return
    for next in range(len(data[here])):
        if (NotVistied(next) or distance[here]+1 < distance[next]) and data[here][next]==1:
            visited[next]=True

            distance[next] = distance[here] +1
            dfs(next)


for time in range(10):
    N, start_point = map(int, input().split())
    nodes = list(map(int, input().split()))
    data = [[0 for _ in range(max(nodes) + 1)] for _ in range(max(nodes) + 1)]

    Q = []
    visited = [0] * (max(nodes) + 1)
    distance = [0] * (max(nodes) + 1)

    for start_to in range(len(nodes) // 2):
        start = nodes[2 * start_to]
        to = nodes[2 * start_to + 1]
        data[start][to] = 1

    dfs(start_point)

    max_dis = max(distance)
    for idx in range(len(distance) - 1, -1, -1):
        if distance[idx] == max_dis:
            ans = idx
            break
    print(ans)