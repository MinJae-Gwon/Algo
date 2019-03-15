# 배열에 정수들이 저장되어 있다. 연속된 구간들 중 그 합이 가장 큰 구간의 합을 찾고 구간을 구하는 알고리즘을 작성하라.
# data = [1,2,-11,4]
data= [5,1,-4,2,-1,-5,-2,8,-3,6]
range_sum = [0]*len(data)
range_sum[0] = data[0]
now = 1
while True:
    if now == len(data):
        break
    range_sum[now] = max(range_sum[now-1]+data[now], data[now])
    now+=1
print(range_sum)

max_range_sum = 0
for i in range(len(range_sum)):
    if range_sum[i] > max_range_sum:
        max_range_sum = range_sum[i]
        max_range_idx = i



