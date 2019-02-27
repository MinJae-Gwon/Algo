import sys
sys.stdin = open('opt_path.txt','r')

<<<<<<< HEAD
# prunning


=======
min_sum = 987654321
def pathfinder(y,start, sofar):
    global min_sum,home,dic,end
    if sofar > min_sum:
        return
    if y == N:
        sofar += abs(start[0]-home[0])+ abs(start[1]-home[1])
        if sofar < min_sum:
            min_sum = sofar
            return
    for next_start in range(1,N+1):
        if not visited[next_start]:
            visited[next_start] = True
            next_point = dic[next_start]
            pathfinder(y+1,next_point,sofar + abs(start[0]-next_point[0])+ abs(start[1]-next_point[1]))
            visited[next_start]=False
>>>>>>> 9afd489e632b9dd6a98fdfe6f011ff95da55f592

T = int(input())
for time in range(T):
    min_sum = 987654321
    N = int(input())
    data = list(map(int,input().split()))
    home = data[:2]
    company = data[2:4]
    data = data[4:]
    visited = [0]*(N+1)
    dic={}
    for key in range(N):
        dic[key+1] = [data[2*(key)],data[2*key+1]]
    pathfinder(0,company, 0)
    print(min_sum)
