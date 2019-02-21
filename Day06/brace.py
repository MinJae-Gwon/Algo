import sys

sys.stdin = open('brace.txt','r')

T= int(input())
for time in range(T):
    N = input()
    stack = []
    if ('{' and '}' and '(' and ')') not in N:
        stack.append(-1)
    for ele in N:
        if ele == '{' or ele == '(':
            stack.append(ele)
        elif ele=='}':
            if stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(ele)
            else:
                stack.append(ele)
                break
        elif ele == ')':
            if stack:
                if stack[-1] =='(':
                    stack.pop()
                else:
                    stack.append(ele)
            else:
                stack.append(ele)
                break

    if not stack:
        print(f'#{time+1} 1')
    else:
        print(f'#{time+1} 0')

