import sys

sys.stdin = open('paper.txt','r')

ans = 0
def area(h,v):
    global ans
    if h==a and v==20:
        ans+=1
        return
    if h>a or v>20: return

    area(h+10, v)
    area(h+20, v)
    area(h+20, v+10)

T = int(input())

for time in range(T):
    a = int(input())
    area(0,0)
    print(ans)
    ans=0