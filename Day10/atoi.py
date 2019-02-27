Data = list('42FB')
data= 0

for now in range(len(Data)):
    if '0' <= Data[now] <= '9':
        val = ord(Data[now])-ord('0')

    elif 'A' <= Data[now] <= 'F':
        val = (ord(Data[now]) - ord('A'))+10
    data = data*16 +val
print(data)