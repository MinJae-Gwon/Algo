import sys
import itertools
sys.stdin = open('스타트링크.txt','r')

def calc1(y,x):
    global s_team_total
    s_team_total += data[y-1][x-1]
    s_team_total += data[x-1][y-1]

def calc2(y,x):
    global l_team_total
    l_team_total += data[y-1][x-1]
    l_team_total += data[x-1][y-1]


N = int(input())
data = []
for rows in range(N):
    row = list(map(int,input().split()))
    data.append(row)

player = [ele for ele in range(1,N+1)]

s_team = list(itertools.combinations(player,N//2))

# 다른 팀 같이 구하면 뻑남
# l_team = []
# for s_teams in s_team:
#     sub=[]
#     for player_num in range(1,N+1):
#         if player_num not in s_teams:
#             sub.append(player_num)
#     l_team.append(sub)

min_gap=987654321
for i in range(len(s_team)//2):
    lets_calc1 = s_team[i]
    # lets_calc2 = l_team[i]
    lets_calc2 = s_team[len(s_team)-i-1]


    relation1 = list(itertools.combinations(lets_calc1,2))
    relation2 = list(itertools.combinations(lets_calc2,2))

    s_team_total = 0
    for ele1 in relation1:
        y1,x1 = ele1
        calc1(y1,x1)
    l_team_total = 0
    for ele2 in relation2:
        y2,x2 = ele2
        calc2(y2,x2)

    gap = abs(s_team_total-l_team_total)
    if gap < min_gap:
        min_gap = gap

print(min_gap)