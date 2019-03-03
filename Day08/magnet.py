import sys
sys.stdin = open('magnet.txt','r')

for time in range(10):
    N = int(input())
    data = []
    for rows in range(100):
        row = list(map(int,input().split()))
        data.append(row)

    count=0
    for x in range(100):
        N_found = 'N'
        for y in range(100):
            if data[y][x] == 1:
                N_found = 'Y'
            elif data[y][x] == 2 and N_found == 'Y':
                count+=1
                N_found = 'N'


    print(f'#{time+1} {count}')
