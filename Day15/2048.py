import sys
sys.stdin = open('2048.txt','r')

def NotSafe(x):
    if x < 0 or x >=N:
        return True


T = int(input())
for time in range(T):
    N, where = map(str,input().split())
    N = int(N)

    merged_data = [[0 for _ in range(N)] for _ in range(N)]

    data=[]
    for rows in range(N):
        row = list(map(int,input().split()))
        data.append(row)

    num_found = False
    if where == 'right':
        for y in range(N-1,-1,-1):
            for x in range(N-1,-1,-1):
                if data[y][x] !=0 and not merged_data[y][x]:

                    num_idx = x
                    num = data[y][num_idx]

                    plus = 1
                    while True:
                        next_idx = num_idx + plus

                        if NotSafe(next_idx):
                            data[y][num_idx], data[y][next_idx-1] = data[y][next_idx-1], data[y][num_idx]
                            break
                        if data[y][next_idx] == 0:
                            plus += 1
                        elif data[y][next_idx] == num:
                            data[y][next_idx] *= 2
                            merged_data[y][next_idx] = True
                            data[y][num_idx] = 0
                            break
                        elif data[y][next_idx] != num:
                            data[y][next_idx-1], data[y][num_idx] = data[y][num_idx], data[y][next_idx-1]
                            break
    print(data)


