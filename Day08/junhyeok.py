import sys
sys.stdin = open('junhyeok.txt','r')

min_sum = 987654321
def pathfinder(y, sofar):
    global min_sum, n
    if sofar > min_sum:
        return
    if y == n:
        if sofar < min_sum:
            min_sum = sofar
        return
    for next_point in range(n+1):
        if data[y][next_point] != 0 and not visited[next_point]:
            visited[y] = True
            pathfinder(next_point,sofar + data[y][next_point])
            visited[y] = False


n,m = map(int,input().split())
data = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0]*(n+1)
for link in range(m):
    start, to, cost = map(int,input().split())
    data[start][to] = cost
pathfinder(1,0)
print(min_sum)
