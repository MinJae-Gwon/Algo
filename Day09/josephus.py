import sys
sys.stdin = open('josephus.txt','r')

Q=[0]*100
people = 5
front = -1
rear = -1

for who in range(1,people+1):
    rear+=1
    Q[rear]=who

while front + 2 != rear:
    front+=1
    alive1 = Q[front]
    front+=1
    alive2 = Q[front]
    front+=1
    dead = Q[front]

    rear+=1
    Q[rear] = alive1
    rear+=1
    Q[rear] = alive2

print(Q[front+1],Q[rear])
    