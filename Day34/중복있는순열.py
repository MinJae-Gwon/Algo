data = ['+','-','*','/']
index_fuel=[4,1,0,0]
#data길이
N=4
#뽑을 개수
M=5
A=[0]*M
def go(now_index):
    global N,M
    if now_index==M:
        print(A)
        return

    for i in range(0,N):
        if index_fuel[i]>0:
            index_fuel[i]=index_fuel[i]-1
            A[now_index]=data[i]
            go(now_index+1)
            index_fuel[i]=index_fuel[i]+1
go(0)