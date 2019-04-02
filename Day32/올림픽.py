import sys
sys.stdin = open('올림픽.txt','r')

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    poll=[0]*len(A)
    for i in range(len(B)):
        for j in range(len(A)):
            if A[j] <= B[i]:
                poll[j]+=1
                break
    max_poll = 0

    for candid in range(len(poll)):
        if poll[candid] > max_poll:
            max_poll = poll[candid]
            max_poll_idx = candid

    print('#{0} {1}'.format(time+1,max_poll_idx+1))