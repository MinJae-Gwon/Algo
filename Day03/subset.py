import sys

sys.stdin = open('subset.txt','r')

l=list(map(int,input().split()))

n = len(l)
zero = 0

# i = (1<<5) = 32 = 1 0 0 0 0 0

#
#0 ~ 31

# i=>
#   0 0 00000 ~ 0 11111

# 10110
#
# 10111

# j 00000
#     ~
#     10000
#
#     00000
#     00001
#     00010
#     00100
#     01000
#     10000
#
#
# 0~4

for i in range(1<<n):
    sum=0
    zero = 0
    temp=[]
    for j in range(n):
        if i & (1 <<j):
            sum+=l[j]
        else:
            zero+=1

    if zero==10:
        pass
    elif sum== 0:
        print(True)