
my_map=[]
my_map.append([1,2,3,4,5])
my_map.append([6,7,8,9,10])
my_map.append([11,12,13,14,15])
my_map.append([16,17,18,19,20])
my_map.append([21,22,23,24,25])




N=5

def rotate():
    global N

    my_map_second = []
    for i in range(0, 5):
        line = [0] * 5
        my_map_second.append(line)

    for y in range(0, N):
        for x in range(0, N):
            my_map_second[y][x] = my_map[x][N-1-y]


    return my_map_second



for z in my_map:
    print(z)

print("ASDASD")

my_map = rotate()

for z in my_map:
    print(z)
