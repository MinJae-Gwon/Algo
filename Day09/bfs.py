import sys
sys.stdin = open('bfs.txt','r')
# order=[]
# def bfs(m,v):
#     global ans
#     q = []
#     q.append(v)
#     visited[v]=True
#     while q:
#         t = q.pop(0)
#         order.append(t)
#         for i in range(len(m[t])):
#             if m[t][i] != 0 and not visited[i]:
#                 q.append(i)
#                 visited[i] = True
#                 parent[i-1] = t
#                 distance[i-1] = distance[parent[i-1]]+1


N = list(map(int,input().split()))
visited = [0]*(max(N)+1)
distance =[0]* (max(N))
parent =[0] * (max(N))
mymap = [[0 for _ in range(max(N)+1)] for _ in range(max(N)+1)]
for idx in range(len(N)//2):
    mymap[N[2*idx]][N[2*idx+1]] = 1
bfs(mymap,1)
print(order)
print(parent)
print(distance)

front=-1
rear=-1
def BFS(here):
    global front,rear
    rear+=1
    Q[rear]=here
    visited[here]=True

    while fromt != rear:
       front+=1
       here = Q[front]
       print(here)

       for next in range(8):
           if MyMap[here][next] and not visited[next]:
               visited[next]=True
               Distance[next] = Distance[here]+1
               Parent[next] = here
               rear+=1
               Q[rear] = next