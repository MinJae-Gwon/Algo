Q=[0]*10000
front = -1
rear = -1

rear+=1; Q[rear] =1
rear+=1; Q[rear] =2
rear+=1; Q[rear] =3

while front != rear:
    front+=1
    print(Q[front])
