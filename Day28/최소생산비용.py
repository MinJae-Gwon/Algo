import sys
sys.stdin = open('최소생산비용.txt','r')

def work_order(deep,sofar):
    global min_cost
    if sofar >= min_cost:
        return
    if deep==N:
        if sofar < min_cost:
            min_cost = sofar
        return
    for next_task in range(N):
        if work_done[next_task] ==0:
            work_done[next_task] = True
            work_order(deep+1,sofar+data[deep][next_task])
            work_done[next_task] = 0

T = int(input())
for time in range(T):
    N = int(input())
    data = []
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)
    work_done = [0]*N
    min_cost = 9887654321

    for task in range(N):
        work_done[task] = True
        work_order(1,data[0][task])
        work_done[task] = 0
    print('#{0} {1}'.format(time+1,min_cost))