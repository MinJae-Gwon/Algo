# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다. -> 중복순열

import sys
sys.stdin = open('NM8.txt','r')

def R_combi(deep,start):
    if deep==M:
        print(*temp)
        return
    for next_num in range(start,N+1):
        temp[deep] = data[next_num-1]
        R_combi(deep+1,next_num)


T=int(input())
for time in range(T):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    data=sorted(data)
    temp=[0]*M

    R_combi(0,1)