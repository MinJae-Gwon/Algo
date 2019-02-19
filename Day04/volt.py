import sys
sys.stdin = open('volt.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    num = list(map(int,input().split()))
    l=[]
    for split in range(N):
        l.append(num[2*split:2*split+2])

    first = 0
    while True:
        count=[]
        l[0], l[first] = l[first], l[0]
        for t in range(len(l)):
            for c in range(len(l)):
                if l[t][1] == l[c][0]:
                    l[t+1], l[c] = l[c], l[t+1]













