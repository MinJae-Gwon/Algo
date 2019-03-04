import sys
sys.stdin  = open('palin2.txt','r')

for time in range(10):
    testcase = int(input())
    data = []
    for rows in range(100):
        row = list(input())
        data.append(row)

    is_done = False
    max_ans=0
    for y in range(100):
        for x in range(100):
           for i in range(100,x,-1):
                comp = data[y][x:i]
                if comp == list(reversed(comp)):
                    if len(comp) > max_ans:
                        max_ans = len(comp)
                        break

    for y_idx in range(100):
        for x_idx in range(100):
            if y_idx > x_idx:
                data[y_idx][x_idx], data[x_idx][y_idx] = data[x_idx][y_idx], data[y_idx][x_idx]

    for y in range(100):
        for x in range(100):
            for i in range(100,x,-1):
                comp = data[y][x:i]
                if comp == list(reversed(comp)):
                    if len(comp) > max_ans:
                        max_ans = len(comp)
                        break

    print('#{0} {1}'.format(time+1,max_ans))
