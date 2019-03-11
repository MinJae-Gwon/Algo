class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

head = None
def enqueue(n):
    global head
    if head == None:
        head = Node(n)
    else:
        parent = None
        p = head
        while True:
            if p.data > n:
                print("와꾸")
                parent.link = Node(n)
                parent.link.link = p
                break
            elif p.link == None:
                print('뺴액')
                p.link = Node(n)
                break
            else:
                print("민박")
                parent = p
                p = p.link

def delete(target):
    p = head
    while True:
        if p.link.data == target:
            break
        p = p.link
    p.link = p.link.link

enqueue(1)
print('---')
enqueue(5)
print('---')
enqueue(2)
print('---')
enqueue(4)
print('---')
enqueue(3)
delete(2)
enqueue(2)
print(head.link.data)
# while True:
#     print(p.data)
#     p = p.link
#     if p.link == None:
#         print(p.data)
#         break


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
#
# node1.link = node2
# node2.link = node3
# node3.link = node4
# node4.link = node5
#
# head = node1
#
# p = head
#
# while p:
#     print(p.data)
#     p = p.link


