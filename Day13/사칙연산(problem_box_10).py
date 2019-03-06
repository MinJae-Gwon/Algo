import sys
sys.stdin = open('사칙연산.txt','r')

ans=[]
def inorder(T):
    global ans
    if T:
        inorder(mymap[T][2])
        inorder(mymap[T][3])
        ans.append(mymap[T][1])

for time in range(10):
    N = int(input())

    mymap = [[0 for _ in range(4)] for _ in range(N+1)]
    for i in range(1,N+1):
        node = list(input().split())
        if len(node) > 3:
            mymap[i][0] = int(node[0])
            mymap[i][1] = node[1]
            mymap[i][2] = int(node[2])
            mymap[i][3] = int(node[3])
        else:
            mymap[i][0] = int(node[0])
            mymap[i][1] = int(node[1])

    inorder(1)

    stack=[]
    while True:
        ele = ans.pop(0)
        if ele == '+':
            num1 =stack.pop()
            num2 = stack.pop()
            stack.append(num2 + num1)
        elif ele == '-':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 - num1)
        elif ele == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 * num1)
        elif ele == '/':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(int(num2 / num1))
        else:
            stack.append(ele)

        if len(ans)==0:
            res = stack[0]
            break

    print('#{0} {1}'.format(time+1,res))
