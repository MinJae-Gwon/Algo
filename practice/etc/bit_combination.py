A = [1,2,3]

for i in range(1<<3):
    for j in range(3):
        if i & (1<<j):
            print(A[j], end=' ')
    print()