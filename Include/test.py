import modele.player as player
from modele.match import Match
from modele.tour import Tour
from modele.tournament import Tournament
from datetime import datetime


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

round = round_control(STATIC_LIST_PLAYER, 'ROUND 1')
list_test = round.list_matches_result
print(list_test)