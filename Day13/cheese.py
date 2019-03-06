import sys
sys.stdin = open('cheese.txt','r')

M,N = map(int,input().split())
data=[]
for rows in range(N):
    row = list(map(int,input().split()))
    data.append(row)


