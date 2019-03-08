import sys
sys.stdin = open('diag_sum.txt','r')

T = int(input())
for time in range(T):
    N, K = map(int,input().split())
    data = []
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)
    dx = [-1,1,-1,1]
    dy = [-1,1,1,-1]
    if K%2==1:
        min_sub = 987654321
        for y in range((K-1)//2,N-K+2):
            for x in range((K-1)//2,N-K+2):
                left_num_sum=0
                right_num_sum=0
                left_num_sum+=data[y][x]
                right_num_sum+=data[y][x]
                for dir in range(len(dx)):
                    if dir < 2:
                        i=1
                        while True:
                            left_num_sum+=data[y+dy[dir]*i][x+dx[dir]*i]
                            i += 1
                            if i > (K-1)//2:
                                break

                    elif dir >=2:
                        j=1
                        while True:
                            right_num_sum += data[y + dy[dir*j]][x + dx[dir*j]]
                            j+=1
                            if j > (K-1)//2:
                                break

                sub = abs(left_num_sum-right_num_sum)
                if sub < min_sub:
                    min_sub = sub
        print('#{0} {1}'.format(time+1,min_sub))

    elif K%2==0:
        min_sub = 987654321
        for start_y in range(N - K + 1):
            for start_x in range(N - K + 1):
                l_sum = 0
                r_sum = 0
                i=0
                while True:
                    l_sum+=data[start_y+1*i][start_x+1*i]
                    i+=1
                    if i ==K:
                        break
                j=0
                while True:
                    r_sum += data[start_y + 1 * j][start_x+(K-1) - 1 * j]
                    j += 1
                    if j == K:
                        break

            sub = abs(l_sum - r_sum)
            if sub < min_sub:
                min_sub = sub
        print('#{0} {1}'.format(time + 1, min_sub))