import sys

sys.stdin = open('color.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    area = [[0 for _ in range(10)] for _ in range(10)]

    for idx in range(N):
        r1,c1,r2,c2,color = map(int,input().split())
        for y in range(c1,c2+1):
            for x in range(r1,r2+1):
                if area[y][x] ==0:
                    area[y][x] = color
                elif area[y][x] != color:
                    area[y][x] = -1
    count = 0
    for y in range(10):
        for x in range(10):
            if area[y][x] == -1:
                count+=1
    print(f'#{time+1} {count}')








