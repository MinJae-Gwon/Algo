import sys
sys.stdin = open('merge_sort.txt','r')

def merge(l,r):
    global cnt
    result=[]
    if l[-1] > r[-1]:
        cnt+=1
    while True:
        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
        if len(l)==0 or len(r)==0:
            break
    if len(l)>0:
        result.extend(l)
    if len(r)>0:
        result.extend(r)
    return result

def merge_sort(A):
    if len(A) <=1:
        return A
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

T = int(input())
for time in range(T):
    N = int(input())
    data = list(map(int,input().split()))
    cnt=0

    print('#{0} {1} {2}'.format(time+1,merge_sort(data)[N//2],cnt))
