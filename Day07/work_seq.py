import sys
sys.stdin = open('work_seq.txt', 'r')

for time in range(10):
    V, E = map(int,input().split())
    link = list(map(int,input().split()))
    # map에 찍기
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for idx in range(len(link)//2):
        data[link[2*idx]][link[2*idx+1]] = 1

    no_input = []
    ans = []
    while True:

        for x in range(1, len(data)):
            sum_col = 0
            for y in range(1, len(data)):
                sum_col += data[y][x]

            if sum_col == 0:
                no_input.append(x)

        topo = no_input.pop(0)
        if not topo in ans:
            ans.append(topo)

        for erase_x in range(V+1):
            if data[topo][erase_x] == 1:
                data[topo][erase_x] = 0

        for erase_y in range(V+1):
            data[erase_y][topo] = -10

        if len(ans) == V:
            break

    ans = ' '.join(map(str,ans))
    print(f'#{time+1} {ans}')





