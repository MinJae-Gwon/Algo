#0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기

import sys
sys.stdin = open('7bit.txt','r')

for time in range(2):
    data = list(map(int,input().split())
    
    sum_num = 0
    for i in range(len(data)):
        sum_num += a&(1<<i)
        if i%7 == 0:
            print(sum_num)
            sum_num = 0

        


