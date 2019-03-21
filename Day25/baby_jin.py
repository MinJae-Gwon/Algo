import sys
sys.stdin = open('baby_jin.txt','r')

def player1_jin(l):
    global player1_is_jin
    player1_counting_sort = [0]*(max(player1_deck)+1)

    for i in range(len(player1_deck)):
        player1_counting_sort[player1_deck[i]] +=1

    for triple in range(len(player1_counting_sort)):
        if player1_counting_sort[triple] >= 3:
            player1_is_jin = True
            return True

    for run in range(len(player1_counting_sort)-2):
        is_run = True
        for idx in range(3):
            if player1_counting_sort[run+idx]==0:
                is_run = False
                break
        if is_run == True:
            player1_is_jin = True
            return True

def player2_jin(l):
    global player2_is_jin
    player2_counting_sort = [0]*(max(player2_deck)+1)

    for i in range(len(player2_deck)):
        player2_counting_sort[player2_deck[i]] +=1

    for triple in range(len(player2_counting_sort)):
        if player2_counting_sort[triple] >= 3:
            player2_is_jin = True
            return True

    for run in range(len(player2_counting_sort)-2):
        is_run = True
        for idx in range(3):
            if player2_counting_sort[run+idx]==0:
                is_run = False
                break
        if is_run == True:
            player2_is_jin = True
            return True



T = int(input())
for time in range(T):
    data = [ele for ele in map(int,input().split())]

    player1_deck=[]
    player2_deck=[]

    player1_is_jin = False
    player2_is_jin = False
    for card in range(len(data)):
        if card%2==0:
            player1_deck.append(data[card])
            if player1_jin(player1_deck) == True:
                print('#{0} {1}'.format(time+1,1))
                break

        else:
            player2_deck.append(data[card])
            if player2_jin(player2_deck) == True:
                print('#{0} {1}'.format(time+1,2))
                break

    if player1_is_jin == False and player2_is_jin == False:
        print('#{0} {1}'.format(time + 1, 0))
