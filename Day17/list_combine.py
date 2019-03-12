import sys
sys.stdin = open('list_combine.txt','r')

class Node:
    def __init__(self,data,link=None):
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
                p.link == Node(n)
                break
            p = p.link

T = int(input())
for time in range(T):
    head = None
    N, M = map(int,input().split())
    for rows in range(M):
        row = list(map(int,input().split()))
        if head == None:
            for ele in row:
                enq(ele)
        else:
            p=head
            target = row[0]
            while True:
                if p.link.data == target:
                    for ele in row:
                        p.link = Node(ele)
                        p=p.link
                    p.link =


