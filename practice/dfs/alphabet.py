import sys
sys.stdin = open('alphabet.txt','r')

def IsSafe(y,x):
    if x>=0 and x<C and y>=0 and y<R:
        return True

def pathfinder(here_y, here_x, sofar):
    global max_path
    
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    for dir in range(len(dy)):
        next_y = here_y + dy[dir]
        next_x = here_x + dx[dir]
        if IsSafe(next_y,next_x) and data[next_y][next_x] not in visited:


R,C = map(int,input().split())
data = []
for rows in range(R):
    row = list(input())
    data.append(row)
visited = []
max_path = 0
pathfinder(0,0,1)