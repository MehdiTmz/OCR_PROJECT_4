from re import L
import modele.player as player
import view.view as view

def match_result_control(player1,player2,state):
    if(state == 1):
        score1 = 1
        score2 = 0

    elif(state == 2): 
        score1 = 0
        score2 = 1

    else: 
        score1 = 0,5
        score2 = 0,5
    return ([player1,score1],[player2,score2])

'''list = view.View.player_data()
print(list)
my_player = player.Player()
my_player.set_player_data(list)
print(my_player.rank)'''
LIST_PLAYER = []
ROUND1_RESULT = []
for x in range(8):
    print(x)
    TEMP = player.Player('player' +str(x),x,x,x,x)
    LIST_PLAYER.append(TEMP)
for y in range(4):
    STATE_POSSIBLE = view.View.match_result_view()
    ROUND1_RESULT.append(match_result_control(LIST_PLAYER[y],LIST_PLAYER[y+4], STATE_POSSIBLE))

MATCH_RESULT = match_result_control(LIST_PLAYER[0],LIST_PLAYER[1],STATE_POSSIBLE)

print(ROUND1_RESULT)