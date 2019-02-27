import sys
sys.stdin = open('rotate.txt','r')

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    Q=[0]*10000
    front=-1
    rear=-1
    l = list(map(int,input().split()))
    for num in range(len(l)):
        rear+=1
        Q[rear] = l[num]

    i=0
    while i <= M:
        front+=1
        ele = Q[front]
        rear+=1
        Q[rear] = ele
        i+=1
    print(f'#{time+1} {Q[front]}')