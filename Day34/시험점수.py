import sys
sys.stdin = open('시험.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    score = list(map(int,input().split()))



