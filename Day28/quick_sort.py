#퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.

import sys
sys.stdin = open('quick_sort.txt','r')

def quick(A,l,r):
    if l>=r:
        return
    pivot = A[l]
    i = l
    j = r

    while i<j:
        while i<j and pivot <= A[j]:
            j-=1
        while i<j and pivot >= A[i]:
            i+=1

        if i<j:
            A[i], A[j] = A[j], A[i]

    A[l], A[i] = A[i], A[l]
    quick(A,l,i-1)
    quick(A,i+1,r)


T = int(input())
for time in range(T):
    N = int(input())
    data = list(map(int,input().split()))

    quick(data,0,len(data)-1)
    print('#{0} {1}'.format(time+1,data[N//2]))