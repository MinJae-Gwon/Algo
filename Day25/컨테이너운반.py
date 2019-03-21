import sys
sys.stdin = open('컨테이너운반.txt','r')

T = int(input())
for time in range(T):
    N,M = map(int,input().split())
    w = [cargo for cargo in map(int,input().split())]
    t = [truck for truck in map(int,input().split())]

    if len(w) > len(t):
        leng = len(t)
    else:
        leng = len(w)

    res = 0

    i=0
    while True:
        max_cargo = 0
        for cargo in range(len(w)):
            if w[cargo] >= max_cargo:
                max_cargo = w[cargo]
                max_cargo_idx = cargo

        truck_is_avail = False
        min_loss = 987654321
        for truck in range(len(t)):
            if t[truck] >=max_cargo:
                truck_is_avail = True
                if t[truck]-max_cargo < min_loss:
                    min_loss = t[truck]-max_cargo
                    min_loss_truck_idx = truck

        if truck_is_avail:
            res+=max_cargo
            t[min_loss_truck_idx] =0
            w[max_cargo_idx]=0
        elif not truck_is_avail:
            w[max_cargo_idx] = 0
        i+=1
        if i==leng:
            break

    print('#{0} {1}'.format(time+1,res))


