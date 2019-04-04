import sys
sys.stdin = open('연산자.txt','r')

def calc(l):
    #l:최종식
    sofar=0
    for idx in range(len(l)-1):
        if idx==0:
            sofar+=l[idx]
        elif idx%2==1:
            if l[idx]=='+':
                sofar+=l[idx+1]
            elif l[idx]=='-':
                sofar-=l[idx+1]
            elif l[idx]=='*':
                sofar*=l[idx+1]
            elif l[idx]=='/':
                sofar = int(sofar/ l[idx + 1])

    return sofar


def make_equation(sign,number):
    equation = [0]*(2*N-1)

    #숫자 배치
    for n in range(len(number)):
        equation[2*n] = number[n]
    #연산자 배치
    for s in range(len(sign)):
        equation[2*s+1] = sign[s]

    res=calc(equation)
    return res


def permu(c):
    global temp,max_ans,min_ans
    if c==N-1:
        #temp: 연산자의 순열, num:주어진 숫자 -> 식만드는 과정

        ans=make_equation(temp,nums)

        if ans > max_ans:
            max_ans=ans
        if ans < min_ans:
            min_ans=ans
        return

    for i in range(4):
        if sign_fuel[i]>0:
            sign_fuel[i]=sign_fuel[i]-1
            temp[c]=signs[i]
            permu(c+1)
            sign_fuel[i]=sign_fuel[i]+1


T = int(input())
for time in range(T):
    N = int(input())
    signs = ['+','-','*','/']
    sign_fuel = list(map(int,input().split()))

    nums = list(map(int,input().split()))

    max_ans = -999999999999999999999999999
    min_ans = 9876543219999999999999999999

    temp=[0]*(N-1)
    permu(0)
    print('#{0} {1}'.format(time+1,max_ans-min_ans))
