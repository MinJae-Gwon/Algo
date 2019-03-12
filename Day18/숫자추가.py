import sys
sys.stdin = open('숫자추가.txt','r')

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


def enq(n):
    global head
    if head==None:
        head = Node(n)
    else:
        p = head
        while True:
            if p.link == None:
                p.link = Node(n)
                break
            p = p.link

def insert(index,n):
    global head
    p=head
    if index == 0:
        minjae = Node(n)
        minjae.link = head
        head = minjae
    else:
        i=0
        while True:
            if i == index-1:
                minjae = Node(n)
                minjae.link = p.link
                p.link = minjae
                break
            p = p.link
            i+=1


T = int(input())
for time in range(T):
    head = None
    N, M, L = map(int,input().split())
    data = list(map(int,input().split()))

    for ele in range(len(data)):
        enq(data[ele])

    for contents in range(M):
        idx, content = map(int,input().split())
        insert(idx,content)

    p=head
    while True:
        if p.link == None:
            break
        p = p.link

    p=head
    i=0
    while True:
        if i == L:
            print('#{0} {1}'.format(time+1,p.data))
            break
        p = p.link
        i+=1

