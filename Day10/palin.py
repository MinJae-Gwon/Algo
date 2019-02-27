import sys
sys.stdin = open('palin.txt','r')

T = int(input())
for time in range(T):
    W = input()
    check =''
    for i in range(len(W)):
        check = W[i] + check

    if check == W:
        print('Yes')
    else:
        print('No')
