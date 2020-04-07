import sys
sys.stdin = open('괄호 짝짓기.txt','r')

for time in range(1,11):
    L = int(input())
    braces = list(input())
    # print(braces)

    # dict 선언
    dic = {
        '[': 0,
        '(': 0,
        '{': 0,
        '<': 0,
    }

    for i in range(len(braces)):
        brace = braces[i]
        if brace == '[' or brace == '(' or brace == '{' or brace == '<':
            dic[brace] +=1

        elif brace == ']':
            dic['['] -= 1
        elif brace == ')':
            dic['('] -= 1
        elif brace == '}':
            dic['{'] -= 1
        elif brace == '>':
            dic['<'] -= 1

    # print(dic)

    matched = True
    for value in dic.values():
        if value != 0:
            matched = False
            break

    if matched == False:
        print('#{0} {1}'.format(time, 0))
    else:
        print('#{0} {1}'.format(time, 1))
