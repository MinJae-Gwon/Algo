import sys
import copy
sys.stdin = open('토마토.txt','r')

def IsSafe(z,y,x):
    if y>=0 and y<N and x>=0 and x<M and z>=0 and z<H:
        return True

def not_all_ripe():
    for i in range(H):
        for j in range(N):
            for q in range(M):
                if box[i][j][q] == 0:
                    return False

def bfs(z,y,x):
    global how_many

    cnt = 0
    visit[z][y][x] = 1

    Q = []
    data = [z,y,x]
    Q.append(data)

    dz = [-1,1]
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    #while Q:

    data = Q.pop(0)
    z = data[0]
    y = data[1]
    x = data[2]

    for z_dir in range(2):
        n_z = z + dz[z_dir]
        if IsSafe(n_z,0,0) and box[n_z][y][x] != -1 and box[n_z][y][x] == 0 and visit[n_z][y][x] == 0:
            #visit[n_z][y][x] = 1
            c_box[n_z][y][x] = 1
            Q.append([n_z,y,x])
            cnt+=1

    for dir in range(4):

        n_y = y + dy[dir]
        n_x = x + dx[dir]

        if IsSafe(0,n_y,n_x) and box[z][n_y][n_x] != -1 and box[z][n_y][n_x] == 0 and visit[z][n_y][n_x] == 0:
            #visit[z][n_y][n_x] = 1
            c_box[z][n_y][n_x] = 1
            Q.append([z, n_y, n_x])
            cnt+=1



M,N,H = map(int,input().split())

already_ripe = True
box = []
for floor in range(H):
    each_floor = []
    for rows in range(N):
        row = list(map(int,input().split()))
        each_floor.append(row)
        if 0 in row:
            already_ripe = False
    box.append(each_floor)
# print(box)

visit = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
c_box = copy.deepcopy(box)
how_many = 0
ripe=1
while True:


    no_more = False
    for i in range(H):
        for j in range(N):
            for q in range(M):
                if box[i][j][q] == 1 and visit[i][j][q] == 0:
                    ripe = bfs(i,j,q)
                    if ripe == 0:
                        no_more = True
                        break
            if no_more == True:
                break
        if no_more == True:
            break
    if no_more == True:
        break
    box = c_box
    how_many += 1




if already_ripe == True:
    print(0)
else:
    if not_all_ripe() == False:
        print(-1)
    else:
        print(how_many)
