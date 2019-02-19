import sys
sys.stdin = open('sub.txt','r')

T = int(input())
for time in range(T):
    N,K = map(int,input().split())
    A = [x for x in range(1,13)]

    #subset
    count=0
    for i in range(1<<12):
        temp = []
        for j in range(12):
            if i & (1<< j):
                temp.append(A[j])
        if len(temp)==N and sum(temp)==K:
            count+=1

    print(f'#{time+1} {count}')