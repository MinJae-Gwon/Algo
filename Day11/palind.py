import sys
sys.stdin = open('palind.txt','r')

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    data = []
    for rows in range(N):
        row = list(input())
        data.append(row)

    ans=[]
    # horizontal
    for y in range(N):
        for i in range(N-M+1):
            if data[y][i:M+i] == list(reversed(data[y][i:M+i])):
                ans = data[y][i:M+i]
                break

    vertical =[]
    for x in range(N):
        for y in range(N-M+1):
            for j in range(M):
                vertical.append(data[y+j][x])
            if vertical == list(reversed(vertical)):
                ans = vertical
                break
            else:
                vertical =[]
        if vertical:
            break

    ans = ''.join(ans)
    print('#{0} {1}'.format(time+1,ans))

