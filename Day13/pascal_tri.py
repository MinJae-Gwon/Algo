import sys
sys.stdin = open('pascal_tri.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    data = []
    ele =[]
    for i in range(1,N+1):
        if i == 1:
            data.append([1])
        elif i ==2:
            data.append([1,1])
        else:
            for j in range(i):
                if j==0 or j==i-1:
                    ele.append(1)

                else:
                    ele.append(data[i-2][j-1] + data[i-2][j])
            data.append(ele)
            ele=[]
    print('#{0}'.format(time+1))
    for row in data:
        row = list(map(str,row))
        row = ' '.join(row)
        print(row)

