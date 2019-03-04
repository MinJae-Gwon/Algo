Pattern = 'abcdabd'
Pattern = list(Pattern)
NEXT = [0]*(len(Pattern))
PI = [0]*(len(Pattern))

PI[0] = -1
PI[1] = 0
i = 0
j = 1

while j != len(Pattern)-1:
    if Pattern[i] != Pattern[j]:
        if i:
            i=0
        else:
            j+=1
            PI[j] =0

    elif Pattern[i] == Pattern[j]:
        if i:
            PI[j + 1] = PI[j] + 1
        else:
            PI[j+1] = 1
        i+=1
        j+=1

print(PI)

str2 = 'abc abcdab abcdabcdabde'

K=0
i=0
PI_move =0
while K!=len(Pattern):
    if str2[i+K] == Pattern[K]:
        K+=1
    else:
        PI_move = K-PI[K]
        i+=PI_move
        k=0
    if i+len(Pattern) > len(str2):
        break

print(i)