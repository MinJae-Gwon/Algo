import sys

sys.stdin = open('단조증가.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    data = list(map(int,input().split()))
    permu = []

    for ele1 in range(len(data)):
        for ele2 in range(len(data)):
            if ele1 != ele2:
                mul = data[ele1]*data[ele2]
                permu.append(mul)

    max_num = 0
    for ele in permu:
        valid = True
        if ele <=10:
            continue
        else:
            now = ele
            while now >=10:
                num1 = now % 10
                now = now // 10
                num2 = now%10

                if num1 < num2:
                    valid = False
                    break

            if valid:
                if ele > max_num:
                    max_num = ele

    if max_num ==0:
        print('#{0} {1}'.format(time+1,-1))
    else:
        print('#{0} {1}'.format(time + 1, max_num))


