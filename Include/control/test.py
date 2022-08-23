
from Include.modele.player import Player
from Include.modele.match import Match
from Include.modele.round import Round
from Include.modele.tournament import Tournament
from datetime import datetime
from createTournamentMenu import CreateTournamentMenu
from Include.view.view import View
from tinydb import TinyDB, Query
import random

RANK = [
    1, 2, 3, 4, 5, 6, 7, 8
]

random.shuffle(RANK)

STATIC_LIST_PLAYER = [
                        Player('player'+str(1), 'name', 'test', 'H', RANK[0]),
                        Player('player'+str(2), 'name', 'test', 'H', RANK[1]),
                        Player('player'+str(3), 'name', 'test', 'H', RANK[2]),
                        Player('player'+str(4), 'name', 'test', 'H', RANK[3]),
                        Player('player'+str(5), 'name', 'test', 'H', RANK[4]),
                        Player('player'+str(6), 'name', 'test', 'H', RANK[5]),
                        Player('player'+str(7), 'name', 'test', 'H', RANK[6]),
                        Player('player'+str(8), 'name', 'test', 'H', RANK[7])]


view = View()
test = CreateTournamentMenu(view)
test.get_tournament_info(STATIC_LIST_PLAYER)
#print(test.tournament.players)
test.round_1('Round 1')
test.round_x('Round 2')
test.round_x('Round 3')
test.round_x('Round 4')
test.tournament.update_score_list()
print(test.tournament.tournament_score)




