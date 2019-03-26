#백준 2263번

import sys
sys.setrecursionlimit(10000)
sys.stdin = open('트리의순회.txt','r')

def GetSome(in_start, in_end, post_start, post_end):
    global res
    if in_start > in_end or post_start > post_end:
        return
    if in_start==in_end or post_start==post_end:
        res.append(in_order[in_start])
        return
    root = post_order[post_end]
    res.append(root)
    in_root = in_order.index(root)

    howmanyleft = in_root - in_start

    GetSome(in_start, in_root-1, post_start, post_start+howmanyleft-1)
    GetSome(in_root+1, in_end, post_start+howmanyleft, post_end-1)

N=int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
res=[]

GetSome(0,N-1,0, N-1)
print(*res)

