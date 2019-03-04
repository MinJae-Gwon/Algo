import sys
sys.stdin = open('GNS.txt','r')

dic1={
"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9
}
dic2={
0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"
}

T = int(input())
for time in range(T):
    testcase_num, testcase = map(str,input().split())
    data = list(map(str,input().split()))

    for i in range(len(data)):
        data[i] = dic1[data[i]]

    data = sorted(data)

    for j in range(len(data)):
        data[j] = dic2[data[j]]

    data = ' '.join(data)
    print(testcase_num,data)