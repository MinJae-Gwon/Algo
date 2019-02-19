import sys

sys.stdin = open('selection_sort.txt','r')

l= list(map(int,input().split()))

start=0
while True:
    min_num = 987654321
    for i in range(start, len(l)):
        if l[i] < min_num:
            min_num = l[i]
            min_num_idx = i
    l[start],l[min_num_idx] = l[min_num_idx], l[start]
    start += 1

    if start == len(l)-1:
        break
print(l)