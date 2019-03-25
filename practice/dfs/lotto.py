import sys
sys.stdin = open('lotto.txt','r')

def combi(deep,start):
    if deep==M:
        print(*temp)
        return
    
    for next_num in range(start+1,N+2):
        temp[deep] = data[next_num-2]
        combi(deep+1,next_num)


while True:
    info = list(map(int,input().split()))
    N = info[0]
    M = 6
    data = info[1:]
    temp=[0]*M

    if N==0:
        break
    
    combi(0,1)
    print()
