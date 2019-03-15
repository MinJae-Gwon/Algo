import sys
sys.stdin = open('1996_rectangle.txt','r')

data = [[0 for _ in range(101)] for _ in range(101)]
for datas in range(4):
    left_x_idx, left_y_idx, right_x_idx, right_y_idx = map(int,input().split())

    for y in range(left_y_idx, right_y_idx):
        for x in range(left_x_idx, right_x_idx):
            if data[y][x] == 0:
                data[y][x] =1
cnt=0
for y_idx in range(101):
    for x_idx in range(101):
        if data[y_idx][x_idx] ==1:
            cnt+=1
print(cnt)
