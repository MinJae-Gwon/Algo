import sys
sys.stdin = open('indorder.txt','r')

ans =''
def inorder(T):
    global ans
    if T:
        inorder(mymap[T][1])
        ans += mymap[T][3]
        inorder(mymap[T][2])


for time in range(10):
    N = int(input())
    mymap = [[0]*4 for _ in range(N+1)]

    for nodes in range(N):
        node = list(input().split())
        for ele in range(len(node)):
            if ele ==1:
                mymap[int(node[0])][3] = node[ele]
            elif ele==2:
                mymap[int(node[0])][1] = int(node[ele])
            elif ele==3:
                mymap[int(node[0])][2] = int(node[ele])
            elif ele==0:
                mymap[int(node[0])][0] = int(node[ele])

    inorder(1)
    print('#{0} {1}'.format(time+1, ans))
    ans=''