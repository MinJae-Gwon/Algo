# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다. -> 조합

import sys
sys.stdin = open('NM2.txt','r')

def combination(deep,start):
    global temp
    if deep==M:
        print(temp)
        return
    for nexta in range(start,N+1):
        # if visited[nexta]==0:
            # visited[nexta] =True
        temp[deep] = nexta
        combination(deep+1,nexta+1)
            # visited[nexta] = 0

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    visited = [0]*(N+1)
    
    temp=[0]*M
    combination(0,1)