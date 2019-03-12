import sys
sys.stdin = open('list_edit.txt','r')

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def enq(n):
    global head
    if head == None:
        head = Node(n)
    else:
        p = head
        while True:
            if p.link == None:
                p.link = Node(n)
                break
            p = p.link

def insert(index, n):
    global head
    p = head
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

def delete(index):
    global head
    if index == 0:
        head = head.link
    else:
        p = head
        i=0
        while True:
            if i == index-1:
                p.link = p.link.link
                break
            p = p.link
            i+=1

def switch(index, n):
    global head
    p = head
    i = 0
    while True:
        if i == index:
            p.data = n
            break
        p = p.link
        i+=1


T = int(input())
for time in range(T):
    head=None
    N, M, L = map(int,input().split())
    data = list(map(int,input().split()))

    for nodes in range(N):
        enq(data[nodes])


    for infos in range(M):
        info = list(input().split())
        type = info[0]
        if type == 'I':
            idx = int(info[1])
            num = int(info[2])
            insert(idx, num)

        elif type == 'D':
            idx = int(info[1])
            delete(idx)

        else:
            idx1 = int(info[1])
            num = int(info[2])
            switch(idx1,num)

    # p = head
    # while True:
    #     print(p.data)
    #     if p.link == None:
    #         break
    #     p = p.link

    p=head
    i =0
    while True:
        if i == L:
            print('#{0} {1}'.format(time+1,p.data))
            break
        if p.link == None:
            print('#{0} {1}'.format(time + 1, -1))
            break
        p = p.link
        i+=1
