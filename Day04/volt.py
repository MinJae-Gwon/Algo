import sys
sys.stdin = open('volt.txt','r')

T = int(input())
for time in range(T):
    N = int(input())
    num = list(map(int,input().split()))

    count = [0]*(max(num)+1)
    for number in num:
        count[number] +=1

    for count_one in range(len(count)):
        if count[count_one] == 1 and num.index(count_one)%2 == 0:
            start = count_one
        if count[count_one] == 1 and num.index(count_one)%2 == 1:
            end = count_one

    volts = []
    for split in range(N):
        volts.append(num[2 * split:2 * split + 2])

    for end_start in range(len(volts)):
        if volts[end_start][1] == end:
            volts[-1], volts[end_start] = volts[end_start], volts[-1]
        if volts[end_start][0] == start:
            volts[0], volts[end_start] = volts[end_start], volts[0]



    std=0
    j=1
    ans=[]
    while True:
        if volts[j][0] == volts[std][1]:
            volts[std+1], volts[j] = volts[j], volts[std+1]
            std+=1
            ans.append(volts[std])
            j=std+1
        else:
            j+=1


        if len(ans) == len(volts)-2:
            break

    fin = []
    for volt in volts:
        volt_male = str(volt[0])
        volt_female = str(volt[1])
        fin.append(volt_male)
        fin.append(volt_female)

    fin = ' '.join(fin)
    print(f'#{time+1} {fin}')









