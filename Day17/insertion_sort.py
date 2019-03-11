data = [3,9,1,6,7,0,4,9,5,5]

for j in range(1,len(data)):
    i = j-1
    while i > -1:
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
            j-=1
            i-=1
        else:
            break
print(data)





