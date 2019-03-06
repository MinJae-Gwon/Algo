import sys
sys.stdin = open('valid_calc.txt','r')

ans = 1
def preorder(T):
    global ans
    if T:
        if mymap[T][1] == '+' or mymap[T][1] =='-' or mymap[T][1] =='/' or mymap[T][1] =='*':
            if int(mymap[T][2])==0 or int(mymap[T][3])==0 :
                ans = 0
                return
        preorder(mymap[T][2])
        preorder(mymap[T][3])


for time in range(10):
    N = int(input())
    mymap = [[0]*5 for _ in range(N+1)]

    for nodes in range(N):
        node = list(input().split())
        for ele in range(len(node)):
            mymap[int(node[0])][0] = int(node[0])
            if ele == 1:
                mymap[int(node[0])][1] = node[ele]
            elif ele == 2:
                mymap[int(node[0])][2] = int(node[2])
                mymap[int(node[2])][4] =  int(node[0])
            elif ele == 3:
                mymap[int(node[0])][3] = int(node[3])
                mymap[int(node[3])][4] = int(node[0])

    preorder(1)
    print('#{0} {1}'.format(time+1,ans))
    ans=1