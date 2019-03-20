import sys
sys.stdin = open('동철이의일분배.txt','r')

max_poten = 0
def combo(deep, sofar):
    global poten,N, max_poten
    if deep==N:
        if sofar > max_poten:
            max_poten = sofar
            
        return
    
    for task in range(N):
        if visited[task] ==0:
            visited[task] =True
            combo(deep+1, sofar*data[deep][task])
            visited[task] = 0
        


T = int(input())
for time in range(T):
    N = int(input())
    
    visited = [0]*N
    data=[]
    for infos in range(N):
        info = list(map(int,input().split()))
        data.append(info)

    combo(0,1)
    print(max_poten)
    # print(poten)
    # res = max(poten)
    # res = res*(0.01**2)
    # print('#%d %0.6f'%(time+1,res))