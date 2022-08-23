from modele.player import Player
from modele.match import Match
from modele.tour import Tour
from modele.tournament import Tournament
from datetime import datetime
from collections import defaultdict


STATIC_LIST_PLAYER = [
                        Player('player'+str(1), 'name', 'test', 'H', 1),
                        Player('player'+str(2), 'name', 'test', 'H', 2),
                        Player('player'+str(3), 'name', 'test', 'H', 3),
                        Player('player'+str(4), 'name', 'test', 'H', 8),
                        Player('player'+str(5), 'name', 'test', 'H', 5),
                        Player('player'+str(6), 'name', 'test', 'H', 6),
                        Player('player'+str(7), 'name', 'test', 'H', 7),
                        Player('player'+str(8), 'name', 'test', 'H', 4)]
print('List_OK')

def round_control(players, name):

    round = Tour(name=name,list_player_pair=players)
    for x in range(4):
        round.list_matches_result.append(Match(round.list_player_pair[x][0],round.list_player_pair[x][1]).match_result(int(input())))
    return round

def create_list_player_pair_round_1(players : list = []):

    players.sort(key=lambda x: x.rank, reverse=False)
    list_pair_1 = []
    for x in range(4):
        list_pair_1.append(players[x::4])
    return list_pair_1

def score_update(round_result, actual_tour_score :list = []):



        print('Error')
LIST_PLAYER = create_list_player_pair_round_1(STATIC_LIST_PLAYER)
print(LIST_PLAYER)
round_1 = round_control(LIST_PLAYER,'Round 1')
print(round_1.list_matches_result)
LIST_PLAYER = score_update(round_1.list_matches_result)
print(score_update(round_1.list_matches_result))
print(LIST_PLAYER['match_list'])
print(LIST_PLAYER['score'])
round_2 = round_control(LIST_PLAYER['match_list'],'Round 2')
print(round_2.list_matches_result)
LIST_PLAYER = score_update(round_2.list_matches_result)
print('Round 2', LIST_PLAYER)
print('Round 2', LIST_PLAYER)



