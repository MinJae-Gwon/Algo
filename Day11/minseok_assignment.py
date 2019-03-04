import sys
sys.stdin = open('minseok_assignment.txt','r')

T = int(input())
for time in range(T):
    N,K = map(int,input().split())
    finish = list(map(str,input().split()))

    all_class = [str(i) for i in range(1,N+1)]

    ans=[]
    for student in all_class:
        if student not in finish:
            ans.append(student)

    ans = ' '.join(ans)
    print('#{0} {1}'.format(time+1,ans))