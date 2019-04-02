import sys
import itertools
sys.stdin = open('스타트링크.txt','r')

def calc(l):
    y,x = l
    return data[y-1][x-1]+data[x-1][y-1]


def combi(c,idx):
    global min_cnt
    #종료조건
    if c==N//2:
        t1=[]
        t2=[]
        for index in range(N):
            if visited[index]==1:
                t1.append(index+1)
            else:
                t2.append(index+1)

        sub1 = list(itertools.combinations(t1,2))
        sub2 = list(itertools.combinations(t2,2))

        sum1=0
        sum2=0
        for idx in range(len(sub1)):
            sum1+=calc(sub1[idx])

            sum2+=calc(sub2[idx])

        gap = abs(sum1-sum2)

        if gap < min_cnt:
            min_cnt = gap

        return

    #조합시작
    for i in range(idx,N):
        visited[i]=1
        combi(c+1,i+1)
        visited[i]=0

N = int(input())
data=[]
for rows in range(N):
    row = list(map(int,input().split()))
    data.append(row)

min_cnt=987654321
visited =[0]*N
combi(0,0)
print(min_cnt)