def power1(a,b):
        res=1
        for time in range(b):
                res*=a
        return res

def power2(a,b):
    if b==0: return 1
    elif b==1: return a
    elif b&1: return a*power2(a,b-1) #b가 홀수이면
    else:
        temp = power2(a,b//2)
        return temp*temp

def power3(a,b): #O(logn)
    ans = 1
    while b>0:
        if b&1: 
                ans*=a #b가 홀수이면
        a = a*a
        b//=2
    return ans


print(power1(2,3))
print(power2(2,100))
print(power3(2,100))