import sys
sys.stdin = open('이진탐색.txt','r')

def binary_search(l,r,target,status):
    global cnt
    m = (l+r)//2
    if l>r:
        return
    
    if A[m] == target:
        cnt+=1
        return
    if status==1 and A[m] < target:
        return
    if status==2 and A[m] > target:
        return
    

    elif A[m] < target:
        binary_search(m+1,r,target,1)
    elif A[m] > target:
        binary_search(l,m-1,target,2)

T = int(input())
for time in range(T):
    N,m = map(int,input().split())

    A = sorted(list(map(int,input().split())))
    M = sorted(list(map(int,input().split())))
    
    cnt=0
    for M_ele in M:
        binary_search(0,len(A)-1,M_ele,0)
        
    print('#{0} {1}'.format(time+1,cnt))