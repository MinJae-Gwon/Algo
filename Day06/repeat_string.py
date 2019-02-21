import sys

sys.stdin = open ('repeat_string.txt','r')

T = int(input())
for time in range(T):
    N = list(input())
    stack=[]
    for i in range(len(N)):
        if not stack:
            stack.append(N[i])
        else:
            if N[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(N[i])
    print(f'#{time+1} {len(stack)}')