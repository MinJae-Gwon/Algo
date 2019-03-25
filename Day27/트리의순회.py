#백준 2263번

import sys
sys.stdin = open('트리의순회.txt','r')

def D_C(A,l,r):
    global res



T = int(input())
for time in range(T):
    N=int(input())
    data = list(map(int,input().split()))
    res=[]
    D_C(data,0,len(data)-1)
    print(res)