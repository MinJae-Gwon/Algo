data = [9,8,5,7,2]
howmany = len(data)
IDT= [0] *(1<<5)

def update(a,b):
    where = base + a - 1
    IDT[where] = b
    where >>= 1

    while where:
        IDT[where] = IDT[where*2] + IDT[where*2 +1]
        where >>=1

def RSQ(ffrom, to):
    ffrom = ffrom + base -1
    to = to + base
    sum = 0

    while ffrom < to:
        if ffrom%2==1:
            sum+=IDT[ffrom]
            ffrom+=1
        if to%2==0:
            sum+=IDT[to]
            to-=1
        ffrom >>= 1; to>>=1

    if ffrom == to : sum += IDT[ffrom]
    return sum


base = 1
while base < howmany:
    base <<=1

for now in range(base, howmany+base):
    IDT[now] = data.pop(0)

for parent in range(base-1,0,-1):
    IDT[parent] = IDT[parent*2] + IDT[parent*2+1]

print(IDT)
print(RSQ(3,8))