import sys
sys.stdin = open('quick_sort.txt','r')

def quick(A,l,r):

    if l>=r:
        return
    pivot = A[l]
    i = l
    j = r

    while i<j:
        while i<j and A[j] >= pivot:
            j-=1
        while i<j and A[i] <= pivot:
            i+=1

        if i<j:
            A[i], A[j] = A[j], A[i]


    A[i], A[l] = A[l], A[i]

    quick(A,l,i-1)
    quick(A,i+1,r)








T = int(input())
for time in range(T):
    data = list(map(int,input().split()))

    quick(data,0,len(data)-1)
    print(data)

