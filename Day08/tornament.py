import sys
sys.stdin = open('tornament.txt','r')

def rps(a,b):
    if a-b ==1:
        return a
    elif a-b == 2:
        return b
    elif a-b == -1:
        return b
    elif a-b == -2:
        return a
    elif a == b:
        return a


def tor(start,end):
    global N, data
    if end == start:
        return data[start]

    split = (start+end)//2
    return rps(tor(start,split),tor(split+1,end))


T = int(input())
for time in range(T):
    N = int(input())
    data = [0]+list(map(int,input().split()))
    print(tor(1,N))



