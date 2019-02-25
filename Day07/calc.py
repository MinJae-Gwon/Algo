import sys

sys.stdin = open('calc.txt', 'r')

isp = [-1]*128
isp[ord('*')] = 2
isp[ord('/')] = 2
isp[ord('+')] = 1
isp[ord('-')] = 1
isp[ord('(')] = 0

icp = [-1]*128
icp[ord('*')] = 2
icp[ord('/')] = 2
icp[ord('+')] = 1
icp[ord('-')] = 1
icp[ord('(')] = 3

for time in range(10):
    length = int(input())
    N = list(input())
    stack = []
    ans = []
    for i in range(len(N)):
        if not stack:
            stack.append(N[i])

        else:
            if N[i] == ')':
                while True:
                    pop = stack.pop()
                    if pop == '(':
                        break
                    else:
                        ans.append(pop)
            else:
                if isp[ord(N[i])] == -1:
                    ans.append(N[i])
                else:
                    if icp[ord(N[i])] > isp[ord(stack[-1])]:
                        stack.append(N[i])
                    else:
                        ans.append(stack.pop())
                        stack.append(N[i])

    num_stack = []

    for idx in range(len(ans)):
        if isp[ord(ans[idx])] == -1:
            num_stack.append(ans[idx])
        else:
            if ans[idx] == '+':
                first = int(num_stack.pop())
                second = int(num_stack.pop())
                sum_num = first + second
                num_stack.append(sum_num)
            elif ans[idx] == '*':
                first = int(num_stack.pop())
                second = int(num_stack.pop())
                mul_num = first * second
                num_stack.append(mul_num)

    print(f'#{time+1} {num_stack[0]}')


