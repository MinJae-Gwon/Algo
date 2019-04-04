import sys
sys.stdin = open('공통조상.txt','r')

def bfs(start_node):
    global subtree
    Q.append(start_node)

    while Q:
        here_node = Q.pop(0)
        if mymap[here_node][0]!=0:
            subtree+=1
            Q.append(mymap[here_node][0])
        if mymap[here_node][1]!=0:
            subtree+=1
            Q.append(mymap[here_node][1])


T = int(input())
for time in range(T):
    V, E, node1, node2 = map(int,input().split())

    data = list(map(int,input().split()))
    mymap=[[0 for _ in range(3)] for _ in range(V+1)]

    for i in range(E):
        parent = data[2*i]
        child = data[2*i+1]
        if mymap[parent][0]==0:
            mymap[parent][0]=child
        else:
            mymap[parent][1]=child
        mymap[child][2] = parent

    parent_list1=[]
    while True:
        if mymap[node1][2]==0:
            break

        mom1 = mymap[node1][2]
        parent_list1.append(mom1)
        node1 = mom1

    parent_list2=[]
    while True:
        if mymap[node2][2]==0:
            break

        mom2 = mymap[node2][2]
        parent_list2.append(mom2)
        node2 = mom2

    parent_found=False
    for ele1 in range(len(parent_list1)):
        for ele2 in range(len(parent_list2)):
            if parent_list1[ele1] == parent_list2[ele2]:
                parent_found=True
                common_parent = parent_list1[ele1]
                break
        if parent_found==True:
            break

    subtree=1
    if common_parent==1:
        subtree = V
    else:
        Q=[]
        bfs(common_parent)

    print('#{0} {1} {2}'.format(time+1,common_parent, subtree))