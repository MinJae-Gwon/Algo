import sys
sys.stdin = open('magnet.txt','r')

for time in range(10):
    N = int(input())
    data = []
    for rows in range(100):
        row = list(map(int,input().split()))
        data.append(row)

    cnt=0
    for x in range(100):
        n_found = False
        for y in range(100):
            if data[y][x] == 1:
                n_found = True
            elif data[y][x] == 2 and n_found:
                cnt+=1
                n_found = False

    print(f'#{time + 1} {cnt}')



# 뻑 나는 코드
# for time in range(100):
#     T = int(input())
#     l = []
#     for i in range(T):
#         line = list(input().split())
#         l.append(line)
#
#     # 2차원 배열 오른쪽 90도 회전
#     new_l = []
#     new_line = ''
#     for index in range(T):
#         for jul in l:
#             new_line += jul[index]
#         new_line = list(new_line)
#         new_l.append(new_line)
#         new_line = ''
#     print(new_l)
#
#     # 1,2 하나 있는 줄 없애기
#     idx = 0
#     while idx != len(new_l):
#         ele1 = new_l[idx]
#         if ele1.count('0') == T - 1:
#             new_l.remove(ele1)
#             idx -= 1
#         idx += 1
#     print(new_l)
#
#     # 2(blue)없애기
#     for ele2 in new_l:
#         for index_two, two in enumerate(ele2):
#
#             if two == '1':
#                 break
#             elif two == '2':
#                 ele2[index_two] = '0'
#
#     print(new_l)
#
#     # 1(red)없애기
#     for ele3 in new_l:
#         for index_one in range(-1, -len(ele3), -1):
#             if ele3[index_one] == '2':
#                 break
#             elif ele3[index_one] == '1':
#                 ele3[index_one] = '0'
#     print(new_l)
#
#     # 충돌
#     fin_l = []
#     for ele4 in new_l:
#         ele4 = ''.join(ele4)
#         ele4 = ele4.replace('0', '')
#         fin_l.append(ele4)
#     print(fin_l)
#
#     # 교착
#     deadlock = 0
#     for ele5 in fin_l:
#         count_index = 0
#
#         while True:
#             if count_index > len(ele5) - 2:
#                 break
#             if ele5[count_index] != ele5[count_index + 1]:
#                 count_index += 2
#                 deadlock += 1
#             elif ele5[count_index] == ele5[count_index + 1]:
#                 count_index += 1
#
#     print(f'#{time + 1} {deadlock}')
