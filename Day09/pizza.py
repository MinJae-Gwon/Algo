import sys
sys.stdin = open('pizza.txt','r')

T = int(input())
for time in range(T):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    Q = []
    # 피자리스트 만들기
    all_pizza = []
    for pizza_ele in range(M):
        all_pizza.append([pizza_ele, l[pizza_ele]])
    # 화덕채우기
    for pizza_in in range(N):
        Q.append(all_pizza[pizza_in])
    last_pizza_idx = N

    while True:

        Q[0][1] = Q[0][1] // 2
        if Q[0][1] == 0 and last_pizza_idx < M:
            Q.pop(0)
            Q.append(all_pizza[last_pizza_idx])
            last_pizza_idx += 1

        elif Q[0][1] == 0 and last_pizza_idx >= M:
            Q.pop(0)
        else:
            Q.append(Q.pop(0))

        if len(Q) == 1:
            break
    print(f'#{time + 1} {Q[0][0] + 1}')