import sys
sys.stdin = open('3143_빠른문자열.txt','r')

tc = int(input())

for case in range(1,tc+1):
    A,B = input().split()

    start = 0
    cnt = len(A)

    while True:
        block = A[start:start+len(B)]
        if block == B:
            start += len(B)
            cnt = cnt - len(B) +1
        else:
            start+=1

        if start + len(B) > len(A):
            break

    print(f'#{case} {cnt}')