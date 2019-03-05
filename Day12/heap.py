import sys
sys.stdin = open('heap.txt','r')

T = int(input())
def resultsum(heap,N):
    tmp=0
    while True:
        N=N//2
        if N<=0:
            break
        else:
            tmp+=heap[N]
    return tmp

for time in range(T):
    N = int(input())
    data = list(map(int,input().split()))
    heap=[0]

    for idx in range(len(data)):
        if idx == 0:
            heap.append(data[idx])
        else:
            heap.append(data[idx])
            i =len(heap)-1
            while True:
                if heap[i] < heap[i//2]:
                    heap[i], heap[i//2] = heap[i//2], heap[i]
                else:
                    pass
                i = i//2
                if i < 1:
                    break

    result = resultsum(heap,N)
    print('#{0} {1}'.format(time+1,result))

