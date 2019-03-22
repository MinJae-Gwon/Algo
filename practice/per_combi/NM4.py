# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다. -> 중복조합

import sys
sys.stdin = open('NM4.txt','r')

def R_combination(deep,start):
    if deep==M:
        print(*temp)
        return
    for next_num in range(start,N+1):
        temp[deep] = next_num
        R_combination(deep+1,next_num)

T = int(input())
for time in range(T):
    N,M = map(int,input().split())

    temp=[0]*M
    R_combination(0,1)