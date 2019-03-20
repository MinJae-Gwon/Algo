data = [9,1,6,8,4,3,2,2,0]

def selection_sort(start):
    global data
    if start == len(data)-1:
        return
    min_ele = 987654321
    for idx in range(start,len(data)):
        if data[idx] < min_ele:
            min_ele = data[idx]
            min_idx = idx
    data[start], data[min_idx] = data[min_idx], data[start]
    selection_sort(start+1)

selection_sort(0)
print(data)
