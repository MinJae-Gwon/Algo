import sys
import itertools

sys.stdin = open('단조증가.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    data = list(map(int,input().split()))

