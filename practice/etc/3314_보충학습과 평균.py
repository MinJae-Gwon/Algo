import sys
sys.stdin = open('3314_보충학습과 평균.txt','r')

T = int(input())
for time in range(T):
    score = list(map(int,input().split()))

    score_sum = 0
    for ele in score:
        if ele < 40:
            ele = 40
        score_sum+=ele

    score_ave = int(score_sum/5)
    print('#{0} {1}'.format(time+1, score_ave))