#import modele.player as player
import modele.player as Player
from modele.match import Match
from modele.round import Round
from modele.tournament import Tournament
from datetime import datetime
from collections import defaultdict


STATIC_LIST_PLAYER = [
                        player.Player('player'+str(1), 'name', 'test', 'H', 1),
                        player.Player('player'+str(2), 'name', 'test', 'H', 2),
                        player.Player('player'+str(3), 'name', 'test', 'H', 3),
                        player.Player('player'+str(4), 'name', 'test', 'H', 8),
                        player.Player('player'+str(5), 'name', 'test', 'H', 5),
                        player.Player('player'+str(6), 'name', 'test', 'H', 6),
                        player.Player('player'+str(7), 'name', 'test', 'H', 7),
                        player.Player('player'+str(8), 'name', 'test', 'H', 4)]
print('List_OK')


def round_control(players, name):

    round = Tour(name=name,list_player_pair=players)
    for x in range(0, 8, 2):
        round.list_matches_result.append(Match(round.list_player_pair[x],round.list_player_pair[x+1]).match_result(int(input())))
    return round

def create_list_player_pair_round_1(players : list = []):

    players.sort(key=lambda x: x.rank, reverse=False)
    list_player_pair = players.copy()
    return list_player_pair

def create_tournament_score_board(players : list):

    players_score_board = players.copy()
    for x in range(len(players)):
        players_score_board[x][0] = players[x].name
        players_score_board[x][1] = 0

    return players_score_board

def update_score(list_player_score : list = [], round = []):
    actual_tour_score = []
    for x in range(4):
        actual_tour_score.append(round[x][0])
        actual_tour_score.append(round[x][1])
    actual_tour_score.sort(key=lambda x: x[1], reverse=True)
    print('1',actual_tour_score)
    '''for x in range(8):
        if(str(actual_tour_score[x][0]) in list_player_score.keys()):
            list_player_score[str(actual_tour_score[x][0])] += actual_tour_score[x][1]
    return list_player_score'''

round_1 = round_control(STATIC_LIST_PLAYER, 'Round 1')
#print(round_1.list_matches_result)
list_player_score = create_tournament_score_board(STATIC_LIST_PLAYER)
print(2,update_score(list_player_score, round_1.list_matches_result))
print(3,round_1.list_matches_result)

'''round_2 = round_control(STATIC_LIST_PLAYER, 'Round 2')
print(round_2.list_matches_result)
print(update_score(list_player_score, round_2.list_matches_result))
print(round_2.list_matches_result)'''


'''    if(actual_tour_score == []):
        
        test = []
        for x in range(4):
            actual_tour_score.append(round_result[x][0])
            actual_tour_score.append(round_result[x][1])
        actual_tour_score.sort(key=lambda x: x[1], reverse=True)
        print(actual_tour_score)
        for x in range(0,8,2):
            list_pair_1 = []
            list_pair_1.append(actual_tour_score[x][0])
            list_pair_1.append(actual_tour_score[x+1][0])
            test.append(list_pair_1)
        result = {'match_list': test,'score': actual_tour_score}
        return result'''

    

#print(update_score(create_tournament_score_board(STATIC_LIST_PLAYER)))
