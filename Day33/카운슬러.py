import sys
import itertools
sys.stdin = open('카운슬러.txt','r')

def combi(c,idx):
    global min_v
    if c==N//2:

        v_x = 0
        v_y = 0
        for idx in range(N):
            if visited[idx] ==1:
                v_y += data[idx][0]
                v_x += data[idx][1]
            else:
                v_y -= data[idx][0]
                v_x -= data[idx][1]

        v = v_x**2 + v_y**2

        if v < min_v:
            min_v = v
        return

    for i in range(idx,N):
        visited[i] = 1
        combi(c+1,i+1)
        visited[i] = 0

T = int(input())
for time in range(T):
    N = int(input())

    data=[]
    for infos in range(N):
        loca = list(map(int,input().split()))
        data.append(loca)
    visited = [0]*N
    min_v =99999999999999999999999999999999999999999999
    combi(0,0)
    print('# {0} {1}'.format(time+1,min_v))



