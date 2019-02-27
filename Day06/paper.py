import sys

sys.stdin = open('paper.txt','r')

ans = 0
def area(h):
    global ans
    if h==a:
        ans+=1
        return
    if h>a: return

    area(h+10)
    area(h+20)
    area(h+20)

T = int(input())

for time in range(T):
    a = int(input())
    area(0)
    print(ans)
    ans=0

