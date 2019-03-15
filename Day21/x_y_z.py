# for x in range(1,100):
#     for y in range(1,100):
#         if x<=y:
#             for z in range(1,100):
#                 if y<=z and x+y+z ==100:
#                     print(x,y,z)

# for i in range(1,34):
#     for j in range(i, 34):
#         print(i,j,100-i-j)

visited = [[[0]*100 for _ in range(100)] for j in range(100)]

cnt=0
def recur(x,y,z):
    global cnt
    if x+y+z>100:
        return
    if x>y or y>z:
        return
    if x+y+z == 100:
        cnt+=1
        return

    if visited[x+1][y][z]==False:
        visited[x+1][y][z] =True
        recur(x+1,y,z)
    if visited[x][y+1][z]==False:
        visited[x][y+1][z] = True
        recur(x,y+1,z)
    if visited[x][y][z+1]==False:
        visited[x][y][z+1]=True
        recur(x,y,z+1)


recur(1,1,1)
print(cnt)