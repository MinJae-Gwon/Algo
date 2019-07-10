import sys
import copy
sys.stdin = open('보호필름.txt','r')

def qualified(mymap):
    qual = True

    for x in range(W):
        a_or_b = []
        for y in range(D):
            if not a_or_b:
                a_or_b.append(mymap[y][x])
            elif a_or_b:
                if a_or_b[-1] == mymap[y][x]:
                    a_or_b.append(mymap[y][x])
                elif a_or_b[-1] != mymap[y][x]:
                    a_or_b = []
                    a_or_b.append(mymap[y][x])
            if len(a_or_b)>=K:
                break
        if len(a_or_b) <K:
            qual = False
            break
    return qual


#floor에 요소를 a로 바꿈 -> 0
def a_go(floors):
    global cnt1

    if not floors:
        pass
    else:
        for i in floors:
            floor = [0]*W
            data[i] = floor

    if qualified(data):
        for j in floors:
            data[j] = ori_data[j]
        return len(floors)

    elif not qualified(data):
        for j in floors:
            data[j] = ori_data[j]
        return False

def b_go(floors):
    if not floors:
        pass
    else:
        for i in floors:
            floor = [1] * W
            data[i] = floor

    if qualified(data):
        for j in floors:
            data[j] = ori_data[j]
        return len(floors)

    elif not qualified(data):
        for j in floors:
            data[j] = ori_data[j]
        return False


T=int(input())
for time in range(T):
    D,W,K = map(int,input().split())
    data=[]
    for rows in range(D):
        row = list(map(int,input().split()))
        data.append(row)

    ori_data = copy.deepcopy(data)
    min_cnt=999999999999

    #a약만 쓸 때
    a=[ele for ele in range(D)]
    for i in range(2 ** 4):
        temp = []

        for j in range(4):
            if i & (1 << j):
                temp.append(a[j])

        ins1 = a_go(temp)
        if ins1:
            if ins1 < min_cnt:
                min_cnt = ins1
        elif ins1 == False:
            pass

    # b약만 쓸 때
    b = [ele for ele in range(D)]
    for i in range(2 ** 4):
        temp = []

        for j in range(4):
            if i & (1 << j):
                temp.append(b[j])

        ins2 = b_go(temp)
        if ins2:
            if ins2 < min_cnt:
                min_cnt = ins2
        elif ins2 == False:
            pass

    print('#{0} {1}'.format(time+1,min_cnt))