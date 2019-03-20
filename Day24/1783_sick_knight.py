import sys
sys.stdin = open('1783_sick_knight.txt','r')


N, M = map(int,input().split())

if N == 1:
    print(1)
elif N ==2:
    if M < 7:
        if M%2 ==1:
            print(M//2+1)
        else:
            print(M//2)
    elif M >=7:
        print(4)
elif N >=3:
    if M >=7:
        print(M-2)
    elif M <7:
        if M<=3:
            print(M)
        
        elif M>=4:
            print(4)
        