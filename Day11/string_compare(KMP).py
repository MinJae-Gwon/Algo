import sys
sys.stdin = open('string_compare(KMP).txt','r')

T = int(input())
for time in range(T):
    str1 = list(input())
    str2 = list(input())


    PI = [0] * (len(str1))

    PI[0] = -1
    PI[1] = 0
    i = 0
    j = 1

    while j != len(str1) - 1:
        if str1[i] != str1[j]:
            if i:
                i = 0
            else:
                j += 1
                PI[j] = 0

        elif str1[i] == str1[j]:
            if i:
                PI[j + 1] = PI[j] + 1
            else:
                PI[j + 1] = 1
            i += 1
            j += 1
    ans=0
    K= 0
    i = 0
    PI_move = 0
    while True:
        if str2[i + K] == str1[K]:
            K += 1
        else:
            PI_move = K - PI[K]
            i += PI_move
            k = 0

        if K == len(str1):
            ans=1
            break
        if i + len(str1) > len(str2):
            ans=0
            break

    print('#{0} {1}'.format(time+1,ans))