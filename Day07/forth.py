import sys
sys.stdin = open('forth.txt','r')

T = int(input())
for time in range(T):
    N = list(map(str,input().split()))
    stack =[]

    for i in range(len(N)):
        if N[i] == '.':
            if len(stack) >1:
                stack=[]
                stack.append('error')
                break
            elif not stack:
                stack.append('error')
                break
            elif len(stack)==1:
                break
            else:
                stack.append('error')
                break

        else:
            if N[i] == '+':
                if len(stack) >1:
                    sum_num = int(int(stack.pop())+ int(stack.pop()))
                    stack.append(sum_num)
                else:
                    stack=[]
                    stack.append('error')
                    break
            elif N[i] == '-':
                if len(stack) >1:
                    sub_num = int(int(stack.pop())- int(stack.pop()))
                    stack.append(sub_num)
                else:
                    stack = []
                    stack.append('error')
                    break

            elif N[i] == '*':
                if len(stack) >1:
                    mul_num = int(int(stack.pop())* int(stack.pop()))
                    stack.append(mul_num)
                else:
                    stack = []
                    stack.append('error')
                    break

            elif N[i] == '/':
                if len(stack) >1:
                    div_num = int(int(stack.pop())/ int(stack.pop()))
                    stack.append(div_num)
                else:
                    stack = []
                    stack.append('error')
                    break
            else:
                stack.append(N[i])

    print(f'#{time+1} {stack[0]}')