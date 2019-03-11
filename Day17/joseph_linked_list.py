class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

head = None
def enq(n):
    global head
    if head == None:
        head = Node(n)

    else:
        p = head
        while True:
            if p.link == None:
                if n == 41:
                    print('빼액',p.data)
                    p.link = Node(n)
                    p.link.link = head
                    break
                else:
                    p.link = Node(n)
                    break

            p = p.link

def delete(target):
    global head
    p =head
    if p.data == target:
        head = head.link
    else:
        while True:
            if p.link.data == target:
                p.link = p.link.link
                break
            p = p.link

for i in range(1,42):
    enq(i)

for j in range(1,39):
    if j%3==0:
        delete(j)

i=0
p = head
while True:
    print(p.data)
    p = p.link
    i+=1
    if i > 41:
        break



