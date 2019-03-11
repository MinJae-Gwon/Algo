import sys

sys.stdin = open('binary_search.txt','r')

l=list(map(int,input().split()))

target = 7
start = 0
end = len(l)-1


while True:
    mid = (end + start) // 2
    if l[mid] > target:
        end = mid-1
    elif l[mid] < target:
        start = mid+1
    elif l[mid]==target:
        print(mid)
        break
    if start >= end:
        print('NoResult')
        break


