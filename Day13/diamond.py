import sys
sys.stdin = open('diamond.txt','r')

T = int(input())
for time in range(T):
    N = input()
    mid_len = 4*(len(N))+1
    data=[]
    row1=[]
    row2=[]
    row3=[]

    for row in range(1,6):
        if row==1 or row==5:
            for i1 in range(mid_len):
                if i1%4 == 2:
                    row1.append('#')
                else:
                    row1.append('.')
            data.append(row1)
            row1=[]

        elif row==2 or row==4:
            for i2 in range(mid_len):
                if i2%2==0:
                    row2.append('.')
                else:
                    row2.append('#')
            data.append(row2)
            row2=[]

        elif row ==3:
            for i3 in range(mid_len):
                if i3%4 == 2:
                    row3.append(N[i3//4])
                elif i3%4==0:
                    row3.append('#')
                else:
                    row3.append('.')
            data.append(row3)
    for ele in data:
        ele = ''.join(ele)
        print(ele)
