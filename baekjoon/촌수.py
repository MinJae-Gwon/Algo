import sys
sys.stdin = open('촌수.txt','r')

def dfs(y,deep):
    global res

    if y == B:
        res = deep

    for i in range(N+1):
        if grid[y][i] == 1 and visit[i] == 0:
            visit[i] = 1
            dfs(i,deep+1)
            visit[i] = 0


N = int(input())
A,B = map(int,input().split())
M = int(input())

grid = [[0 for _ in range(N+1)] for _ in range(N+1)]
for rows in range(M):
    start,end = map(int,input().split())
    grid[start][end] = 1
    grid[end][start] = 1

res = -1
visit = [0 for _ in range(N+1)]
visit[A] = 1
dfs(A,0)
print(res)