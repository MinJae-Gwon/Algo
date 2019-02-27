import sys
sys.stdin = open('pizza.txt','r')

T=int(input())
for time in range(T):
    N,M = map(int,input().split())
    l = list(map(int,input().split()))
    Q=[0]*100
    front=-1
    rear=-1
    #피자리스트 만들기
    all_pizza =[0]*M
    for pizza_ele in range(M):
        all_pizza[pizza_ele] = [pizza_ele,l[pizza_ele]]
    # 화덕채우기
    for pizza_in in range(N):
        rear+=1
        Q[pizza_in] = all_pizza[pizza_in]
    last_pizza_idx = M-N


    while True:
        Q[front + 1][1] = Q[front + 1][1] // 2
        if Q[front + 1][1] == 0 and last_pizza_idx < M:
            Q[front+1] = all_pizza[last_pizza_idx]
            last_pizza_idx+=1
            front += 1
            pizza = Q[front]
            rear += 1
            Q[rear] = pizza
        elif Q[front + 1][1] == 0 and last_pizza_idx >= M:
            front+=1
        else:
           front+=1
           pizza = Q[front]
           rear+=1
           Q[rear] = pizza

        if front +1 == rear:
            break
    print(f'#{time+1} {Q[rear][0]+1}')