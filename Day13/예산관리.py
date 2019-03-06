import sys
sys.stdin = open('예산관리.txt','r')

def NotVisited(a):
    if visited[a] == 0:
        return True

max_sofar = 0
def GetSome(sofar):
    global max_sofar
    if sofar >= B:
        return
    if sofar > max_sofar:
        max_sofar = sofar
    for next in A:
        if NotVisited(next):
            visited[next]=True
            GetSome(sofar+next)
            visited[next]=False



B = int(input())
N = int(input())
A = list(map(int,input().split()))
visited = [0]*(max(A)+1)
GetSome(0)
print(max_sofar)
