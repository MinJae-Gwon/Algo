import sys
import itertools
sys.stdin = open('양팔저울.txt','r')

def facto(num):
    r=1
    while num>0:
        r*=num
        num-=1
    return r

def DFS(left_sum, right_sum, cnt):
    global ans
    if right_sum > left_sum:
        return
    if cnt == N:
        ans+=1
        return

    if left_sum >= total-left_sum:
        ans+= 2**(N-cnt)*facto(N-cnt)
        return

    for j in range(N):
        if not visited[j]:
            visited[j]=1
            DFS(left_sum+chu[j], right_sum, cnt+1)
            DFS(left_sum, right_sum+chu[j],cnt+1)
            visited[j]=0
T = int(input())
for time in range(T):

    N = int(input())
    chu = list(map(int,input().split()))
    total=sum(chu)

    ans=0
    for i in range(N):
        visited = [0]* N
        visited[i] = 1
        DFS(chu[i], 0, 1)
    print('#{0} {1}'.format(time+1,ans))



# T = int(input())
# for time in range(T):
#
#     N = int(input())
#     data=list(map(int,input().split()))
#     permu = list(itertools.permutations(data,3))
#     for ele in permu:
#
#         for i in range(2**N):
#             l_idx=[0]*N
#             r_idx=[0]*N
#             for j in range(N):
#                 if i & (1<<j):
#                     #왼쪽 저울에 들어갈 추의 인덱스를 l_idx에 추가하는 작업
#                     l_idx[j]=ele[j]
#             #오른쪽(R) 저울에 들어갈 추의 인덱스를 r_idx에 추가하는 작업
#
#
#         # # 왼쪽 저울을 추로 채우기
#         # for l_ele in range(len(l_idx)):
#         #     if l_idx[l_ele]==-1:
#         #         l_idx[l_ele] = 0
#         #     else:
#         #         l_idx[l_ele] = data[l_idx[l_ele]]
#         # #오른쪽 저울을 추로 채우기
#         # for r_ele in range(len(r_idx)):
#         #     if r_idx[r_ele]==-1:
#         #         r_idx[r_ele] = 0
#         #     else:
#         #         r_idx[r_ele] = data[r_idx[r_ele]]
#         #
#         # if sum(r_idx) > sum(l_idx):
#         #     continue
#
#             print('왼',l_idx)
#             # print('오',r_idx)
#         # print()

