import sys
sys.stdin = open('이진탐색.txt','r')

def binary_search(l,r,target):
    global cnt, l_search_time, r_search_time, ans_found
    m = (l+r)//2
    if l>r:
        return
    if A[m] == target:
        ans_found= True
        return

    elif A[m] < target:
        r_search_time+=1
        binary_search(m+1,r,target)
    elif A[m] > target:
        l_search_time+=1
        binary_search(l,m-1,target)

T = int(input())
for time in range(T):
    N,m = map(int,input().split())

    A = sorted(list(map(int,input().split())))
    M = sorted(list(map(int,input().split())))
    
    cnt=0
    for M_ele in M:
        l_search_time = 0
        r_search_time = 0
        ans_found = False
        binary_search(0,len(A)-1,M_ele)
        if ans_found==True and l_search_time==r_search_time:
            cnt+=1
    print('#{0} {1}'.format(time+1,cnt))