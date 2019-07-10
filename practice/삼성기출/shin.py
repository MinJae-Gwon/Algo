def solutions(value, projects):
    class Node:
        node = {}
        def __init__(self,num,val):
            self.num = num
            self.val = val
            self.lowNode = []
            Node.node[self.num] = self

        def connect(self,other):
            self.lowNode.append(other)

        def getMax(self):
            if not self.lowNode:
                return self.val
            else:
                maxVal = 0
                for low in self.lowNode:
                    maxVal = max(maxVal,low.getMax())
                val = self.val + maxVal
                return val

    for num,val in enumerate(value):
        Node(num+1,val)

    node = Node.node
    for pjt in projects:
        high, low = pjt[0], pjt[1]
        node[high].connect(low)

    return node[1].getMax()