import sys
sys.stdin = open('snake.txt','r')

def out(y,x):
    if y<0 or x<0 or y>=N or x>=N:
        return True
def momtong(y,x):
    if data[y][x] > 0:
        return True

def go(head_y, head_x, tail_y, tail_x, dir):
    global time
    time=0
    dy=[0,1,0,-1]
    dx=[1,0,-1,0]

    while True:
        if time in times:
            dir_idx = times.index(time)
            if directions[dir_idx] == 'D':
                dir = (dir+1)%4
            elif directions[dir_idx] == 'L':
                dir = (dir+3)%4
        n_head_y = head_y + dy[dir]
        n_head_x = head_x + dx[dir]

        if out(n_head_y,n_head_x) or momtong(n_head_y,n_head_x):
            break
        elif data[n_head_y][n_head_x]==-1:
            data[n_head_y][n_head_x] = data[head_y][head_x]+1
            head_y = n_head_y
            head_x = n_head_x
        elif data[n_head_y][n_head_x]==0:

            data[n_head_y][n_head_x] = data[head_y][head_x] + 1
            head_y = n_head_y
            head_x = n_head_x
            for where in range(len(dy)):
                n_tail_y = tail_y + dy[where]
                n_tail_x = tail_x + dx[where]
                if out(n_tail_y,n_tail_x):
                    continue
                if data[tail_y][tail_x]+1 == data[n_tail_y][n_tail_x]:
                    data[tail_y][tail_x]=0
                    tail_y = n_tail_y
                    tail_x = n_tail_x
                    break
        time += 1
        for c in data:
            print(c)

        print('시간',time)
        print('대가리',head_y,head_x)
        print('꼬리', tail_y, tail_x)


N = int(input())
K = int(input())
data=[[0 for _ in range(N)] for _ in range(N)]
for apples in range(K):
    a_y, a_x = map(int,input().split())
    data[a_y-1][a_x-1] = -1

L = int(input())
times=[]
directions=[]
for infos in range(L):
    time, direction = map(str,input().split())
    time = int(time)
    times.append(time)
    directions.append(direction)
data[0][0]=1
go(0,0,0,0,0)
print(time+1)

