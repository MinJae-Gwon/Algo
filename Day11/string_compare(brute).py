import sys
sys.stdin = open('string_compare(brute).txt','r')

T = int(input())
for time in range(T):
    str1 = input()
    str2 = input()

    count =0
    for i in range(len(str2)-len(str1)+1):
        if str2[i:len(str1)+i] == str1:
            count+=1
    print('#{0} {1}'.format(time+1,count))

