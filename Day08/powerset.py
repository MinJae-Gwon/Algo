def powerset(a,k,input):
    if k==input:
        for idx in range(len(a)):
            if a[idx] == 0:
                pass
            else:
                a[idx] = data[idx]
        print(a)
        return
    for zero_one in range(2):
        a[k] =  zero_one
        powerset(a,k+1,input)

data = [1,2,3,4]
start = [0]*len(data)
input=len(data)
powerset(start,0,input)

