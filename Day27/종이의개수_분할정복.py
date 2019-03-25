import sys
sys.stdin = open('종이의개수.txt','r')

def IsSame(y,x,size):
    for y_idx in range(size):
        for x_idx in range(size):
            if data[y+y_idx][x+x_idx] != data[y][x]:
                return False
    return True

def GetSome(y,x,size):
    if IsSame(y,x,size):
        res[data[y][x]+1] += 1
        return
    next=size//3
    for i in range(3):
        for j in range(3):
            GetSome(y+i*next, x+j*next,next)

N = int(input())
data=[]
for rows in range(N):
    row = list(map(int,input().split()))
    data.append(row)

res=[0]*3
GetSome(0,0,9)

for ans in res:
    print(ans)
