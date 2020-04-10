import sys
sys.stdin = open('4530_극한청소.txt','r')


def four_in(floor):
    for i in range(len(floor)):
        if floor[i] == '4':
            return True

tc = int(input())

for case in range(1,tc+1):
    start,to = map(int,input().split())

    cnt = 0
    for floor in range(start+1,to+1):
        if floor == 0:
            continue
        else:
            floor = str(floor)
            if four_in(floor):
                continue
            else:
                cnt+=1
    print(f'#{case} {cnt}')
