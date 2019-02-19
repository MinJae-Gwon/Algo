import sys

sys.stdin = open('textbook.txt','r')

T = int(input())
for time in range(T):
    P,A,B = map(int,input().split())
    textbook = list(x for x in range(1,P+1))

    #A search
    l=0
    r = P-1
    A_search_time = 1
    while True:
        mid = int((l+r)/2)
        if textbook[mid] == A:
            break
        elif textbook[mid] > A:
            r = mid

        elif textbook[mid] < A:
            l = mid

        A_search_time+=1

        if l > r:
            break

    #B search
    l = 0
    r = P - 1
    B_search_time = 1
    while True:
        mid = int((l + r) / 2)
        if textbook[mid] == B:
            break
        elif textbook[mid] > B:
            r = mid

        elif textbook[mid] < B:
            l = mid

        B_search_time += 1

        if l > r:
            break

    if A_search_time > B_search_time:
        print(f'#{time+1} B')
    elif A_search_time < B_search_time:
        print(f'#{time+1} A')
    else:
        print(f'#{time+1} 0')