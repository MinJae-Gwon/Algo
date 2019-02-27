import sys
sys.stdin = open('contact.txt','r')

def Isconnected(a,b):
    if data[a][b] ==1:
        return True
def Isnotvisited(a):
    if not visited[a]:
        return True

def contact(v):
    Q.append(v)
    visited[v] =True
    while Q:
        here = Q.pop(0)
        for next in range(len(data[here])):
            if Isconnected(here,next) and Isnotvisited(next):
                Q.append(next)
                visited[next] = True
                distance[next] = distance[here]+1

for time in range(10):
    N, start_point = map(int,input().split())
    nodes = list(map(int,input().split()))
    data=[[0 for _ in range(max(nodes)+1)] for _ in range(max(nodes)+1)]

    Q=[]
    visited = [0]*(max(nodes)+1)
    distance = [0]*(max(nodes)+1)

    for start_to in range(len(nodes)//2):
        start = nodes[2*start_to]
        to = nodes[2*start_to+1]
        data[start][to] = 1

    contact(start_point)

    max_dis = max(distance)
    for idx in range(len(distance)-1,-1,-1):
        if distance[idx] == max_dis:
            ans = idx
            break
    print(f'#{time+1} {ans}')