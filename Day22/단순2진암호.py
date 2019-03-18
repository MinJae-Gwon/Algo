import sys
sys.stdin = open('단순2진암호.txt','r')

dic = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
}
keys=[]
for key in dic.keys():
    keys.append(key)

T = int(input())
for time in range(T):
    N,M = map(int,input().split())

    info = ''
    for rows in range(N):
        row = input()

        if row=='0'*M:
            pass
        else:
            info = row
    res=[]
    i=0
    while True:
        if info[i:i+7] in keys:
            res.append(dic[info[i:i+7]])
            i+=7
            if i + 7 > len(info):
                break
            elif info[i:i+7] != '0000000' and info[i:i+7] not in keys:
                res.pop()
                i-=6
        else:
            i+=1

        if i+7 > len(info):
            break

    odd_idx = 0
    even_idx = 0
    for idx in range(len(res)):
        if (idx+1)%2 ==1:

            odd_idx+=res[idx]
        elif (idx+1)%2 == 0:

            even_idx+=res[idx]

    valid = odd_idx*3 + even_idx


    if valid%10 ==0:
        print('#{0} {1}'.format(time+1,odd_idx+even_idx))
    else:
        print('#{0} {1}'.format(time+1,0))






