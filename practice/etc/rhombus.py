N = 7

for y in range(N):
    for x in range(N):
        if y <= N//2:
            if x < N//2-y or x > N//2+y:
                print(' ',end='')
            else:
                print('*',end='')
        else:
            if x < N//2-(N-y-1) or x > N//2+(N-y-1):
                print(' ',end='')
            else:
                print('*',end='')
    print()
        