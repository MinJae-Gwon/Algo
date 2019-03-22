#7272. 안경이 없어!
import sys
sys.stdin = open('안경이없어.txt','r')

no_hole = list('CEFGHIJKLMNSTUVWXYZ')
one_hole = list('ADOPQR')

T = int(input())
for time in range(T):
    case1, case2 = map(str,input().split())

    is_same = True
    if len(case1) != len(case2):
        is_same = False
    if is_same:
        for idx in range(len(case1)):
            if (case1[idx] in no_hole and case2[idx] in no_hole) or (case1[idx] in one_hole and case2[idx] in one_hole) or case1[idx] =='B' and case2[idx] =='B':
                is_same = True
            else:
                is_same = False
                break

    if is_same:
        print('#{0} {1}'.format(time+1,'SAME'))
    else:
        print('#{0} {1}'.format(time + 1, 'DIFF'))

    


