data = [38, 27, 43, 3, 9, 82, 10]

def merge(l,r):
    result = []
    while True:
        if l[0] >= r[0]:
            result.append(r.pop(0))
        else:
            result.append(l.pop(0))
        if len(l) == 0 or len(r) == 0:
            break

    if len(l) > 0:
        result.extend(l)
    if len(r) > 0:
        result.extend((r))

    return result



def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)


print(merge_sort(data))