#5C3을 보여라

a = 5
b = 3
data = [ele for ele in range(1,a+1)]
res = [0]*b
visited = [0]*a

for i1 in range(a):
    for i2 in range(i1,a):
        if i1!=i2:
            for i3 in range(i2,a):
                if i2!=i3:
                    
                    res[0] = data[i1]
                    res[1] = data[i2]
                    res[2] = data[i3]
                    print(res)

                
# 3C2
# for i1 in range(a):
#     for i2 in range(i1,a):
#         if i1!=i2:
#             res[0] = data[i1]
#             res[1] = data[i2]
#             print(res)
              