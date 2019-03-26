import sys
sys.stdin = open('전기버스2.txt','r')

def Battery_status(deep,cell,change):
    global min_change
    if change >= min_change:
        return
    if deep==N-1:
        if change < min_change:
            min_change = change
        return

    for go in range(1,cell+1):

        if deep+go < N-1:
            Battery_status(deep + go, data[deep + go], change+1)
        elif deep + go == N - 1:
            Battery_status(deep + go, cell, change)

T = int(input())
for time in range(T):
    info = list(map(int,input().split()))
    N = info[:1][0]
    data = info[1:]+[0]
    min_change = 987654321

    Battery_status(0,data[0],0)
    print(min_change)