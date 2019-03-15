import sys
sys.stdin = open('seive.txt','r')

# 에라토스테네스의 체
start, to = map(int,input().split())

data = [ele for ele in range(to+1)]
data[0] = 0
data[1] = 0
for i in range(2,len(data)):
    j=2
    while True:
        if i*j > to:
            break
        data[i*j] = 0
        j+=1

for idx in range(start,len(data)):
    if data[idx] !=0:
        print(data[idx])