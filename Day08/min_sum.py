import sys
sys.stdin = open('min_sum.txt','r')

def backtrack(y, sofar):
    global N
    global min_sum

    if sofar >= min_sum:
        return
    if y==N:
        if sofar < min_sum:
            min_sum = sofar
            return

    for x in range(N):
        if not visitedX[x]:
            visitedX[x] = True
            backtrack(y+1, sofar + data[y][x])
            visitedX[x] = False



T= int(input())
for time in range(T):
    min_sum = 987654321
    N=int(input())
    data = []
    visitedX = [0] * (N)
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)
    backtrack(0,0)
    print(f'#{time+1} {min_sum}')
