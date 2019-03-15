import sys
sys.stdin = open('1996_number_pick.txt','r')

N = int(input())
idx_list = [ele for ele in range(1,N+1)]
data = []
for elements in range(N):
    element = int(input())
    data.append(element)

while True:
    if set(idx_list) == set(data):
        break
    for num in range(len(idx_list)):
        if idx_list[num] not in data:
            idx_list[num]=0
            data[num]=0

print(len(idx_list) -idx_list.count(0))
for res in idx_list:
    if res !=0:
        print(res)


