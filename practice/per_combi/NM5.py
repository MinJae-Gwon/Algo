# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열

import sys
sys.stdin = open('NM5.txt','r')

def permu(deep):
    if deep==M:
        print(*temp)
        return
    for next_num in range(1,N+1):
        if visited[next_num] ==0:
            visited[next_num]=True
            temp[deep] = data[next_num-1]
            permu(deep+1)
            visited[next_num]=0

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    data = sorted(data)
    visited=[0]*(N+1)
    temp=[0]*M
    
    permu(0)

