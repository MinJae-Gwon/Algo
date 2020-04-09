import sys
sys.stdin = open('7465_무리의개수.txt','r')


def go(person):

    for next_person in range(1,N+1):
        if relation[person][next_person] == 1 and connected[next_person] != True:
            connected[next_person] = True
            go(next_person)

tc = int(input())

for case in range(1,tc+1):
    N,M = map(int,input().split())

    relation = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(M):
        start,to = map(int,input().split())
        relation[start][to] = 1
        relation[to][start] = 1

    cnt = 0
    connected = [False for _ in range(N + 1)]
    for person in range(1,N+1):
        if connected[person] == False:
            connected[person] = True
            go(person)
            cnt +=1

    print(f'#{case} {cnt}')