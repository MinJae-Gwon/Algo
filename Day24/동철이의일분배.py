import sys
sys.stdin = open('동철이의일분배.txt','r')


def combo(deep, sofar):
    global poten,N, max_poten
    if sofar <= max_poten:
        return
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
    max_poten = 0
    visited = [0]*N
    data=[]
    for infos in range(N):
        info = [ele*0.01 for ele in list(map(int,input().split()))]
        data.append(info)

    combo(0,1)
    max_poten = max_poten*100
    print('#',time+1," ", "%0.6f" % max_poten, sep='')
    