import sys

sys.stdin = open('seq_search.txt','r')

l=list(map(int,input().split()))
target = 2

for i in range(len(l)):
    if l[i] == target:
        print(l[i], '검색성공')
        break
    if i == len(l)-1 and l[i] != target:
        print(-1)
        break