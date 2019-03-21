import sys
sys.stdin = open('화물도크.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    #종료시간 이른 것부터 정렬
    data=[]
    for infos in range(N):
        info = list(map(int,input().split()))
        data.append(info)

    start=0
    while True:
        min_num =98765
        for idx in range(start,len(data)):
            if data[idx][1] < min_num:
                min_num = data[idx][1]
                min_num_idx = idx
        data[start], data[min_num_idx] = data[min_num_idx], data[start]
        start+=1
        if start==len(data):
            break

    now_task = data[0]
    progress = 1
    cnt=1
    while True:
        for next_task in range(progress,len(data)):
            if data[next_task][0] >= now_task[1]:
                progress=next_task
                cnt+=1
                now_task = data[next_task]
                break
            else:
                progress+=1
        if progress == len(data):
            break
    print('#{0} {1}'.format(time+1,cnt))