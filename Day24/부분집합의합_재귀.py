#비재귀
# data = [-1,3,-9,6,7,-6,1,5,4,-2]
data=[1,2,3,4]
# for i in range(1<<10):
#     temp=[]
#     for j in range(10):
#         if i & (1<<j):
#             temp.append(data[j])
#     if sum(temp)==0 and len(temp)>=1:
#         print(temp)
    
#재귀

def sub(deep,sofar):
    print(deep,visited)
    if deep == 4:
        print("a",visited)
        return
    if sofar == 0:
        print("b",visited)
        return
    
    
    for i in range(len(data)):
        if visited[i] == 0:
            visited[i] = True
            sub(deep+1, sofar+data[i])
            # sofar-=data[i]
            visited[i] = 0
            sub(deep+1,sofar)


for start in range(len(data)):
    visited = [0]*len(data)
    visited[start] = True
    sub(1,data[start])
    print('빼액')
    visited[start] = 0