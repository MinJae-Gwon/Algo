import sys
sys.stdin = open('othello.txt','r')





T = int(input())
for time in range(T):
    N , M = map(int,input().split())
    data = [[0 for _ in range(N) ]for _ in range(N)]

    data[N//2-1][N//2-1] = 2
    data[N//2-1][N//2] = 1
    data[N//2][N//2-1] = 1
    data[N//2][N//2] = 2

    put_info = []
    for positions in range(M):
        position = list(map(int,input().split()))
        put_info.append(position)

    