import sys
sys.stdin = open('opt_path.txt','r')

def IsNotVisited(a):
    if not visited[a]:
        return True


min_dis = 987654321
def opt(y,here, sofar):
    global min_dis

    visited[here] = True


    if sofar > min_dis:
        return

    if y==N:
        sofar+= abs(data[here][0]-data[-1][0]) + abs(data[here][1]-data[-1][1])

        if sofar < min_dis:
            min_dis = sofar
        return


    for next in range(1,N+1):
        if IsNotVisited(next):
            visited[next]=True
            opt(y+1, next, sofar + abs(data[here][0]-data[next][0]) + abs(data[here][1]-data[next][1]))
            visited[next]=False


T = int(input())
for time in range(T):
    N = int(input())
    l = list(map(int,input().split()))
    home = l[:2]
    company = l[2:4]
    l = l[4:]
    data=[(0,0)]*(N+2)
    for idx in range(len(l)//2):
        node = (l[2*idx],l[2*idx+1])
        data[idx+1] = node

    data[0] = (company[0],company[1])
    data[-1]= (home[0],home[1])

    visited = [0]*(N+2)


    opt(0,0,0)
    print(f'#{time+1} {min_dis}')
    min_dis = 987654321




















# min_sum = 987654321
# def pathfinder(y,start, sofar):
#     global min_sum,home,dic,end
#     if sofar > min_sum:
#         return
#     if y == N:
#         sofar += abs(start[0]-home[0])+ abs(start[1]-home[1])
#         if sofar < min_sum:
#             min_sum = sofar
#             return
#     for next_start in range(1,N+1):
#         if not visited[next_start]:
#             visited[next_start] = True
#             next_point = dic[next_start]
#             pathfinder(y+1,next_point,sofar + abs(start[0]-next_point[0])+ abs(start[1]-next_point[1]))
#             visited[next_start]=False
#
#
# T = int(input())
# for time in range(T):
#     min_sum = 987654321
#     N = int(input())
#     data = list(map(int,input().split()))
#     home = data[:2]
#     company = data[2:4]
#     data = data[4:]
#     visited = [0]*(N+1)
#     dic={}
#     for key in range(N):
#         dic[key+1] = [data[2*(key)],data[2*key+1]]
#     pathfinder(0,company, 0)
#     print(min_sum)
