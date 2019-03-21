#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 -> 순열

import sys
sys.stdin = open('NM1.txt','r')

def permutation(deep):
    global temp
    if deep == M:
        print(*temp)
        return
    for next in range(1,N+1):
        if visited[next] == 0:
            visited[next] =True
            temp[deep] = next
            permutation(deep+1)
            visited[next] =0

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    temp=[0]*(M)
    visited=[0]*(N+1)

    permutation(0)