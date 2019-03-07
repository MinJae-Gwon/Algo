import sys
sys.stdin = open('fly_catch.txt','r')

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    data = []
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)
    max_num = 0
    for y in range(N-M+1):
          for x in range(N-M+1):
              num_sum=0
              for dir_y in range(M):
                  for dir_x in range(M):
                      num_sum+=data[y+dir_y][x+dir_x]
              if num_sum > max_num:
                  max_num = num_sum
    print('#{0} {1}'.format(time+1,max_num))

