import sys
sys.stdin = open('snail.txt','r')

def Issafe(x,y):
    if x>=0 and x<5 and y>=0 and y<5:
        return True
def IsNotVisited(x,y):
    if data[y][x] ==0:
        return True

l = []
for rows in range(5):
    row = list(map(int,input().split()))
    l.extend(row)

i=1
while True:
    for idx in range(len(l)-1):
        if l[idx] > l[idx+1]:
            l[idx], l[idx+1] = l[idx+1], l[idx]
        else:
            pass
    i+=1
    if i == len(l)-1:
        break


data = [[0 for _ in range(5)] for _ in range(5)]
data[0][0]=l[0]
dx = [1,0,-1,0]
dy = [0,1,0,-1]


dir=0
ele=1
x = 0
y = 0
while True:
    new_x = x + dx[dir%4]
    new_y = y + dy[dir%4]
    if Issafe(new_x,new_y) and IsNotVisited(new_x,new_y):
        data[new_y][new_x] = l[ele]
        x = new_x
        y = new_y
        ele+=1
    else:
        dir+=1
    if ele==25:
        break
print(data)