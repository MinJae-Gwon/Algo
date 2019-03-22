# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다. -> 중복순열

import sys
sys.stdin = open('NM3.txt','r')

def R_permutation(deep):
    if deep==M:
        print(*temp)
        return
    for next_num in range(1,N+1):
        temp[deep] = next_num
        R_permutation(deep+1)

T = int(input())
for time in range(T):
    N,M = map(int,input().split())

    temp=[0]*(M)
    R_permutation(0)