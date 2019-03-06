import sys
sys.stdin = open('cheese.txt','r')

def IsDone():
    for y in data:
        if sum(y) == 0:
            return False
    return True

def check():
    status = [True, True]
    for y_idx in range(N):
        for x_idx in range(M):
            if data[y_idx][x_idx]==1 and (sum(data[y_idx][:x_idx]) == 0 or data[y_idx][x_idx+1]==0):
                status[0] = False

    


M,N = map(int,input().split())
data=[]
for rows in range(N):
    row = list(map(int,input().split()))
    data.append(row)


