import sys
import collections

sys.stdin = open('미로.txt','r')

def IsSafe(y,x):
    if y>=0 and y<N and x>=0 and x<M:
        return True

def dfs(y,x,how_far):
    global min_far

    if how_far > min_far:
        return

    if y == N-1 and x == M-1:
        if how_far < min_far:
            min_far = how_far
        return

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    for dir in range(4):
        n_y = y + dy[dir]
        n_x = x + dx[dir]
        if IsSafe(n_y,n_x):
            if maze[n_y][n_x] == 1 and visit[n_y][n_x] == 0:
                if burden[n_y][n_x] == 0 or how_far +1 < burden[n_y][n_x]:
                    visit[n_y][n_x] = 1
                    burden[n_y][n_x] = how_far+1
                    dfs(n_y,n_x,how_far+1)
                    visit[n_y][n_x] = 0



N,M = map(int,input().split())

maze = []
for rows in range(N):
    row = list(map(int,list(input())))
    maze.append(row)

visit = [[0 for _ in range(M)] for _ in range(N)]
visit[0][0] = 1
min_far = 9999999999999

burden = [[9999999999999 for _ in range(M)] for _ in range(N)]
dfs(0,0,1)

print(min_far)

# def bfs(data):
#     Q.append(data)
#
#     dy = [-1, 0, 1, 0]
#     dx = [0,1,0,-1]
#
#     while Q:
#         dataSet = Q.popleft()
#         y = dataSet[0]
#         x = dataSet[1]
#         how_far = dataSet[2]
#
#         for dir in range(4):
#             n_y = y + dy[dir]
#             n_x = x + dx[dir]
#             if IsSafe(n_y,n_x):
#                 if maze[n_y][n_x] == 1 and visit[n_y][n_x] == 0:
#                     visit[n_y][n_x] = 1
#
#
#
# N,M = map(int,input().split())
#
# maze = []
# for rows in range(N):
#     row = list(map(int,list(input())))
#     maze.append(row)

# Q = collections.deque
# visit = [[0 for _ in range(M)] for _ in range(N)]
# visit[0][0] = 1
# min_far = 9999999999999
#
# bfs([0,0,1])