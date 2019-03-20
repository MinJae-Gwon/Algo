N=123
K=7

result =''
while True:
    result = str(N%K) +result
    N=N//K
    if N <=0:
        break
print(result)