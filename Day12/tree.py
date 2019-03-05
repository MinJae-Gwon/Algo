import sys
sys.stdin = open('tree.txt','r')

def preorder(T):
    if T:
        print(T, end=' ')
        preorder(mymap[T][1])
        preorder(mymap[T][2])

def postorder(T):
    if T:
        postorder(mymap[T][1])
        postorder(mymap[T][2])
        print(T, end=' ')

def inorder(T):
    if T:
        inorder(mymap[T][1])
        print(T, end=' ')
        inorder(mymap[T][2])

V = int(input())
data = list(map(int,input().split()))

mymap = []
for rows in range(max(data)+1):
    row = [0]*6
    mymap.append(row)
# mymap[y][1] = left child
# mymap[y][2] = right child
# mymap[y][3] = 자녀수
# mymap[y][4] = 부모
# mymap[y][5] = level

for i in range(0,len(data),2):
    parent = data[i]
    child = data[i+1]
    if mymap[parent][1] == 0:
        mymap[parent][1] = child
    else:
        mymap[parent][2] = child

    mymap[parent][3] += 1
    mymap[child][4] = parent
    mymap[child][5] = mymap[parent][5] +1


print('Pre_Order')
preorder(1)
print('\nPost_Order')
postorder(1)
print('\nIn_Order')
inorder(1)

node = 13
while True:
    if mymap[node][4]==0:
        break
    print('\n',mymap[node][4])
    node = mymap[node][4]



