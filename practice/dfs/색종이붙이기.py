import sys
sys.stdin = open('색종이붙이기.txt','r')


def all_zero():
    no_zero = True
    for y in range(10):
        for x in range(10):
            if field[y][x] == 1:
                no_zero = False
        if not no_zero:
            break
    return no_zero

def how_big(y,x,size):
    flag = True
    for j in range(size):
        for i in range(size):
            if y+j>9 or x+i>9 or field[y+j][x+i] == 0:
                flag = False
        if not flag:
            break
    return flag

def make_zero_one(y,x,size,what):
    for j in range(size):
        for i in range(size):
            field[y+j][x+i] = what


def go(cnt,one,two,three,four,five):
    global min_res

    if cnt >= min_res:
        return

    if one <0 or two<0 or three<0 or four<0 or five<0:
        return

    if all_zero():
        if cnt < min_res:
            min_res = cnt
        return

    for y in range(10):
        for x in range(10):
            if field[y][x] == 1:
                if how_big(y,x,5):
                    make_zero_one(y,x,5,0)
                    go(cnt+1,one,two,three,four,five-1)
                    make_zero_one(y,x,5,1)

                if how_big(y,x,4):
                    make_zero_one(y,x,4,0)
                    go(cnt+1,one,two,three,four-1,five)
                    make_zero_one(y,x,4,1)

                if how_big(y,x,3):
                    make_zero_one(y,x,3,0)
                    go(cnt+1,one,two,three-1,four,five)
                    make_zero_one(y,x,3,1)

                if how_big(y,x,2):
                    make_zero_one(y,x,2,0)
                    go(cnt+1,one,two-1,three,four,five)
                    make_zero_one(y,x,2,1)

                if how_big(y,x,1):
                    make_zero_one(y,x,1,0)
                    go(cnt+1,one-1,two,three,four,five)
                    make_zero_one(y,x,1,1)



field = []
for rows in range(10):
    row = list(map(int,input().split()))
    field.append(row)

min_res = 9999999999

go(0, 5,5,5,5,5)

print(min_res)