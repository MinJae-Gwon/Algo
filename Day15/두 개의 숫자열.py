import sys
sys.stdin = open('두 개의 숫자열.txt','r')

T= int(input())
for time in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N>M:
        compare = N-M+1
        l = A
        s = B
        leng = len(B)
    elif M>N:
        compare = M-N+1
        l = B
        s = A
        leng = len(A)
    else:
        compare = 1
        l = A
        s = B
        leng = len(A)


    max_sum = -99999
    for i in range(compare):
        mul_sum = 0
        for j in range(leng):
            mul_sum += s[j]*l[i+j]
        if mul_sum > max_sum:
            max_sum = mul_sum
    print('#{0} {1}'.format(time+1,max_sum))
