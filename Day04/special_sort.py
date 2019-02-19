import sys

sys.stdin = open('special_sort.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    l=list(map(int,input().split()))
    start=0
    while True:
        min_num = 987654321
        max_num = -1
        for idx_for_max in range(start,len(l)):
            if l[idx_for_max] > max_num:
                max_num = l[idx_for_max]
                max_num_idx = idx_for_max
        l[start], l[max_num_idx] = l[max_num_idx], l[start]

        for idx_for_min in range(start+1,len(l)):
            if l[idx_for_min] < min_num:
                min_num = l[idx_for_min]
                min_num_idx = idx_for_min
        l[start+1], l[min_num_idx] = l[min_num_idx], l[start+1]
        start+=2

        if start > len(l)-1:
            break
    res=[]
    for ele in range(10):
        res.append(l[ele])

    res=' '.join(map(str,res))
    print(f'#{time+1} {res}')


