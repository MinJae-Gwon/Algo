import sys
sys.stdin = open('탈주범.txt','r')

def IsSafe(y,x):
    if x>=0 and y>=0 and x<M and y<N and data[y][x]!=0:
        return True

def bfs(y,x,fuel):
    Q.append(y)
    Q.append(x)
    Q.append(fuel)
    while Q:
        here_y = Q.pop(0)
        here_x = Q.pop(0)
        here_fuel = Q.pop(0)
        next_fuel = here_fuel-1
        # 구조물 타입: 1(십자)
        if data[here_y][here_x]==1:
            dy1=[-1,0,1,0]
            dx1=[0,1,0,-1]

            for dir1 in range(len(dy1)):
                next_y = here_y+dy1[dir1]
                next_x = here_x+dx1[dir1]
                # 구조물이 십자일 때 위쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir1==0 and (data[next_y][next_x]==1 or data[next_y][next_x]==2 or data[next_y][next_x]==5 or data[next_y][next_x]==6):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
                # 구조물이 십자일 때 오른쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir1==1 and (data[next_y][next_x]==1 or data[next_y][next_x]==3 or data[next_y][next_x]==6 or data[next_y][next_x]==7):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
                # 구조물이 십자일 때 아래쪽으로 갈 수 있는 조건
                if IsSafe(next_y, next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir1 == 2 and (data[next_y][next_x]==1 or data[next_y][next_x]==2 or data[next_y][next_x]==4 or data[next_y][next_x]==7):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
                # 구조물이 십자일 때 왼쪽으로 갈 수 있는 조건
                if IsSafe(next_y, next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir1 == 3 and (data[next_y][next_x]==1 or data[next_y][next_x]==3 or data[next_y][next_x]==4 or data[next_y][next_x]==5):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
        # 구조물 타입: 2(세로1자)
        elif data[here_y][here_x]==2:
            dy2=[-1,1]
            dx2=[0,0]

            for dir2 in range(len(dy2)):
                next_y = here_y + dy2[dir2]
                next_x = here_x + dx2[dir2]
                #구조물이 세로1자일 때 위쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir2==0 and (data[next_y][next_x]==1 or data[next_y][next_x]==2 or data[next_y][next_x]==5 or data[next_y][next_x]==6):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
                # 구조물이 세로1자일 때 아래쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir2==1 and (data[next_y][next_x]==1 or data[next_y][next_x]==2 or data[next_y][next_x]==4 or data[next_y][next_x]==7):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
        # 구조물 타입: 3(가로1자)
        elif data[here_y][here_x]==3:
            dy3=[0,0]
            dx3=[1,-1]
            for dir3 in range(len(dy3)):
                next_y = here_y + dy3[dir3]
                next_x = here_x + dx3[dir3]
                # 구조물이 가로1자일 때 오른쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir3==0 and (data[next_y][next_x]==1 or data[next_y][next_x]==3 or data[next_y][next_x]==6 or data[next_y][next_x]==7 or data[next_y][next_x]==3):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
                # 구조물이 가로1자일 때 왼쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir3==1 and (data[next_y][next_x]==1 or data[next_y][next_x]==3 or data[next_y][next_x]==4 or data[next_y][next_x]==5):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
        # 구조물 타입: 4(오른쪽 아래로 대각선)
        elif data[here_y][here_x]==4:
            dy4=[0,-1]
            dx4=[1,0]
            for dir4 in range(len(dy4)):
                next_y = here_y + dy4[dir4]
                next_x = here_x + dx4[dir4]
                # 구조물이 오른쪽 아래로 대각선일 때 오른쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir4==0 and (data[next_y][next_x]==1 or data[next_y][next_x]==3 or data[next_y][next_x]==6 or data[next_y][next_x]==7):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
                # 구조물이 오른쪽 아래로 대각선일 때 위쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir4==1 and (data[next_y][next_x]==1 or data[next_y][next_x]==2 or data[next_y][next_x]==5 or data[next_y][next_x]==6):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
        # 구조물 타입: 5(왼쪽 아래로 대각선)
        elif data[here_y][here_x]==5:
            dy5=[1,0]
            dx5=[0,1]
            for dir5 in range(len(dy5)):
                next_y = here_y + dy5[dir5]
                next_x = here_x + dx5[dir5]
                # 구조물이 왼쪽 아래로 대각선일 때 아래쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir5==0 and (data[next_y][next_x]==1 or data[next_y][next_x]==2 or data[next_y][next_x]==4 or data[next_y][next_x]==7):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
                # 구조물이 왼쪽 아래로 대각선일 때 오른쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir5==1 and (data[next_y][next_x]==1 or data[next_y][next_x]==3 or data[next_y][next_x]==6 or data[next_y][next_x]==7):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
        # 구조물 타입: 6(왼쪽 위로 대각선)
        elif data[here_y][here_x]==6:
            dy6=[1,0]
            dx6=[0,-1]
            for dir6 in range(len(dy6)):
                next_y = here_y + dy6[dir6]
                next_x = here_x + dx6[dir6]
                # 구조물이 왼쪽 위로 대각선일 때 아래쪽으로 갈 수 있는 조건
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir6==0 and (data[next_y][next_x]==1 or data[next_y][next_x]==2 or data[next_y][next_x]==4 or data[next_y][next_x]==7):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
                # 구조물이 왼쪽 위로 대각선일 때 왼쪽으로 갈 수 있는 조건
                if IsSafe(next_y, next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir6 == 1 and (data[next_y][next_x]==1 or data[next_y][next_x]==3 or data[next_y][next_x]==4 or data[next_y][next_x]==5):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
        # 구조물 타입: 7
        elif data[here_y][here_x]==7:
            dy7=[0,-1]
            dx7=[-1,0]
            for dir7 in range(len(dy7)):
                next_y = here_y + dy7[dir7]
                next_x = here_x + dx7[dir7]
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir7==0 and (data[next_y][next_x]==1 or data[next_y][next_x]==3 or data[next_y][next_x]==4 or data[next_y][next_x]==5):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)
                if IsSafe(next_y,next_x) and here_fuel>0 and mymap[next_y][next_x] < next_fuel and dir7==1 and (data[next_y][next_x]==1 or data[next_y][next_x]==2 or data[next_y][next_x]==5 or data[next_y][next_x]==6):
                    mymap[next_y][next_x] = next_fuel

                    Q.append(next_y)
                    Q.append(next_x)
                    Q.append(next_fuel)


T = int(input())
for tc in range(T):
    #터널세로길이:N, 터널가로길이:M, 맨홀위치_y:R, 맨홀위치_x:C, 탈출후시간:L
    N,M,R,C,L = map(int,input().split())

    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)
    mymap = [[0 for _ in range(M)] for _ in range(N)]
    mymap[R][C] = L
    Q=[]
    bfs(R,C,L)
    ans=0
    for y in range(N):
        for x in range(M):
            if mymap[y][x]>=1:
                ans+=1
    print('#{0} {1}'.format(tc,ans))
