import sys
sys.stdin = open('압축풀기.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    data = ''
    for rows in range(N):
        alpha, num = map(str,input().split())
        num = int(num)
        alpha = alpha*num
        data += alpha
    i=0
    res=''
    print('#{0}'.format(time+1))
    while True:
        res+=data[i]
        i+=1
        if i%10==0:
            print(res)
            res=''
        if i==len(data):
            print(res)
            break