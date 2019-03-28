import sys
sys.stdin = open('연산.txt','r')

def bfs(sofar):
    global min_calc_time
    Q.append(sofar)

    while Q:
        here = Q.pop(0)
        if here[0]==target_num:
            if here[1] < min_calc_time:
                min_calc_time = here[1]
            return
        for calc in range(4):
            if here[0] <= 1000000:
                if calc ==2:
                    next = (here[0]+1,here[1]+1)
                    Q.append(next)
                elif calc ==1:
                    if here[0] >target_num:
                        next = (here[0]-1,here[1]+1)
                        Q.append(next)
                elif calc ==0:
                    if here[0] > 0:
                        next = (here[0]*2,here[1]+1)
                        Q.append(next)
                elif calc ==3:
                    if here[0] > 0:
                        next = (here[0]-10,here[1]+1)
                        Q.append(next)

T = int(input())
for time in range(T):
    start_num,target_num = map(int,input().split())
    min_calc_time = 987654321
    Q=[]

    bfs((start_num,0))
    # dfs(0,start_num)
    print('#{0} {1}'.format(time+1,min_calc_time))