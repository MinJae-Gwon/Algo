import sys
sys.stdin=open('이진수2.txt','r')

T=int(input())
for time in range(T):
    N = float(input())

    res = ''
    i=-1
    while True:
        if len(res)>=13:
            res = 'overflow'
            break
        if N==2**i:
            res+='1'
            break
        elif N>2**i:
            res+='1'
            N-=2**i
        else:
            res+='0'
        i-=1
    print('#{0} {1}'.format(time+1, res))