import sys
sys.stdin = open('퇴사.txt','r')

# def dfs(day,sofar):
#     global max_money
#
#     if day > N+1:
#         return
#     if day==N+1:
#
#         if sofar > max_money:
#             max_money = sofar
#         return
#
#     dfs(day+T[day-1],sofar+P[day-1])
#     dfs(day+1,sofar+0)
#
#
# T = int(input())
# for time in range(T):
#     N = int(input())
#     data = [0]*(N)
#     T = [0]*(N)
#     P = [0]*(N)
#
#     for infos in range(N):
#         t,p = map(int,input().split())
#         T[infos] = t
#         P[infos] = p
#
#     max_money = 0
#     dfs(1,0)
#     print(max_money)

def dfs(day,sofar):
    global max_money
    if day > N:
        return
    if day==N:
        if sofar > max_money:
            max_money = sofar
        return

    dfs(day+T[day], sofar+P[day])
    dfs(day+1, sofar)


T = int(input())
for time in range(T):
    N = int(input())
    T=[]
    P=[]
    max_money = 0
    for infos in range(N):
        t,p = map(int,input().split())
        T.append(t)
        P.append(p)

    dfs(0,0)
    print(max_money)