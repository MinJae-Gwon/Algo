import sys
sys.stdin = open('은행.txt', 'r')

T = int(input())
for time in range(T):
    a=list(input())
    b=list(input())
    a=[int(ele) for ele in a]
    b=[int(ele) for ele in b]

    bi = []
    for i in range(len(a)):
        if a[i] ==0:
            a[i] =1
            trans = ''.join([str(ele) for ele in a])
            bi.append(trans)
            a[i] =0
        elif a[i] ==1:
            a[i] =0
            trans = ''.join([str(ele) for ele in a])
            bi.append(trans)
            a[i] =1

    tri =[]
    for j in range(len(b)):
        for zero_one_two in range(3):
            if b[j] == zero_one_two:
                pass
            elif b[j] != zero_one_two:
                dummy = b[:]
                dummy[j] = zero_one_two
                trans = ''.join([str(ele) for ele in dummy])
                tri.append(trans)
    
    bi_res = []
    for ele_bi in bi:
        int_bi =[int(ele) for ele in list(ele_bi)]
        decimal = 0
        for idx in range(len(int_bi)):
            decimal += int_bi[idx]*(2**(len(int_bi)-idx-1))
        bi_res.append(decimal)
    
    tri_res=[]
    for ele_tri in tri:
        int_tri = [int(ele) for ele in list(ele_tri)]
        decimal = 0
        for index in range(len(int_tri)):
            decimal += int_tri[index]*(3**(len(int_tri)-index-1))
        tri_res.append(decimal)
    
    for comp1 in bi_res:
        for comp2 in tri_res:
            if comp1 == comp2:
                print('#{0} {1}'.format(time+1,comp1))
                break
    