dic = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}

# data = '0000110111101100'
data = '0001010111010001110101010001'
keys=[]
for key in dic.keys():
    keys.append(key)
print(keys)

i=0
while True:
    if data[i:i+6] in keys:
        print(dic[data[i:i+6]])
        i+=6
    else:
        i+=1

    if i+5 >= len(data):
        break



