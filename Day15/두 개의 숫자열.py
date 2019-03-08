import sys
sys.stdin = open('두 개의 숫자열.txt','r')

T= int(input())
for time in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

