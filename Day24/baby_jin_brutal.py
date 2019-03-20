num = '101123'
num = [int(ele) for ele in list(num)]
N = [0]*6

Got_It = False
for i1 in range(6):
    for i2 in range(6):
        if i1!=i2:
            for i3 in range(6):
                if i1!=i3 and i2!=i3:
                    for i4 in range(6):
                        if i1!=i4 and i2!=i4 and i3!=i4:
                            for i5 in range(6):
                                if i1!=i5 and i2!=i5 and i3!=i5 and i4!=i5:
                                    for i6 in range(6):
                                        if i1!=i6 and i2!=i6 and i3!=i6 and i4!=i6 and i5!=i6:
                                            N[i1] = num[0]
                                            N[i2] = num[1]
                                            N[i3] = num[2]                                           
                                            N[i4] = num[3]
                                            N[i5] = num[4]
                                            N[i6] = num[5]
                                            if (N[2]-N[1] ==1 and N[1]-N[0]==1 and N[3]==N[4] and N[4]==N[5]) or (N[0]==N[1] and N[1]==N[2] and N[3]==N[4] and N[4]==N[5]) or (N[0]==N[1] and N[1]==N[2] and N[2]==N[3] and N[3]==N[4] and N[4]==N[5]):
                                                Got_It = True
                                                print(N)
                                                print('Baby_Jin')
                                                break
                                if Got_It == True:
                                    break
                        if Got_It == True:
                            break
                if Got_It == True:
                    break
        if Got_It == True:
            break
if Got_It ==False:
    print('No_Baby_Jin')