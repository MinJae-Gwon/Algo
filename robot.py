import sys
import itertools
sys.stdin = open('robot.txt','r')

T=int(input())
for time in range(T):
    N = int(input())
    robot_loca = list(map(int,input().split()))
    snack_loca = list(map(int,input().split()))
    robot=[]
    snack=[]

    for robot_info in range(N):
        robot_y = robot_loca[2*robot_info]
        robot_x = robot_loca[2*robot_info+1]
        robot.append((robot_y,robot_x))

    for snack_info in range(N):
        snack_y = snack_loca[2*snack_info]
        snack_x = snack_loca[2*snack_info+1]
        snack.append((snack_y,snack_x))

    permu = list(itertools.permutations([ele for ele in range(N)],N))

    min_dist = 987654321
    for j in range(len(permu)):
        dist=0
        for i in range(N):
            robot_idx_y, robot_idx_x = robot[i]
            snack_idx_y, snack_idx_x = snack[permu[j][i]]

            dist += abs(robot_idx_x-snack_idx_x) + abs(robot_idx_y-snack_idx_y)
        if dist < min_dist:
            min_dist = dist

    print(min_dist)

