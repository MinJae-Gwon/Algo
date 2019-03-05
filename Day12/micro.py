import sys
sys.stdin = open('micro.txt','r')

T = int(input())

min_count = 987654321
count = 0
i_find=0
def dfs(start):
    global count,t,a,b,min_count, i_find
    if start > t:
        return

    if start == t:

        if count < min_count:
            i_find=1
            min_count = count
        return
    else:
        count+=1

    dfs(start*b)
    dfs(start+a)



for time in range(T):
    s,t,a,b = map(int,input().split())

    dfs(s)
    if i_find==1:
        print('#{0} {1}'.format(time+1,min_count))
    else:
        print('#{0} {1}'.format(time+1,-1))
    count=0
    min_count=987654321
    i_find =0