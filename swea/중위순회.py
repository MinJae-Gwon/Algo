import sys
sys.stdin = open('중위순회.txt','r')

def inorder(T):
    global ans
    if T:
        inorder(mymap[T][2])
        ans += mymap[T][1]
        inorder(mymap[T][3])

for time in range(1,10):
    N = int(input())

    # 트리 테이블 생성
    mymap = [[0]*4 for _ in range(N+1)]

    # 트리 테이블 채우기 : 노드 번호, 알파벳, 왼쪽 자식, 오른쪽 자식
    for i in range(N):
        data = list(input().split())
        for j in range(len(data)):
            if j == 1:
                mymap[int(data[0])][j] = data[j]
            else:
                mymap[int(data[0])][j] = int(data[j])
    print(mymap)

    ans=''
    inorder(1)
    print(ans)

