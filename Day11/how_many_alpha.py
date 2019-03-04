import sys
sys.stdin = open('how_many_alpha.txt','r')

T = int(input())
for time in range(T):
    str1 = input()
    str2 = input()

    dic = {}
    for ele in str1:
        dic[ele] = 0

    for key in dic.keys():
        for alpha in str2:
            if key == alpha:
                dic[key]+=1

    max_num = 0
    for value in dic.values():
        if value > max_num:
            max_num = value

    print('#{0} {1}'.format(time+1,max_num))