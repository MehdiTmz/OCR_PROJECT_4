"""Define tournament controler"""
from Include.modele.player import Player
from Include.modele.match import Match
from Include.modele.round import Round
from Include.modele.tournament import Tournament
from datetime import datetime
from controlTournament import ControlTournament
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

db = TinyDB('db.json')
full_player_list: list[Player] = []
serialized_full_player = []

if db.table('player'):
    players_table = db.table('player')
    for player in players_table:
        player_to_add = Player(player['name'],player['firstname'],
                                player['birthdate'],player['sex'],player['rank'])
        full_player_list.append(player_to_add)
        #players_table.truncate()
else :
    players_table = db.table('player')

if db.table('tournament'):
    tournaments_table = db.table('tournament')
else:
    tournaments_table = db.table('tournament')

def player_selection_control(full_player_list, view):

    players = []

    while len(players) < 8:

        view.tournament_player_selection_display()
        option_player_selection = int(input())

        if option_player_selection == 1:

            player_name = input('Entrez le nom du joueur que vous recherchez :')
            player_found =[]

            for p in full_player_list:
                count = 1
                if p.name == player_name:
                    print(count,': ' + p.name)
                    player_found.append(p)
                    count += 1
                else:
                    print('Aucun joueur trouvé')

            index_player = int(input('Confirmez le joueur : '))
            players.append(player_found[index_player - 1])

        if option_player_selection == 2:

            new_player = view.player_input_view()
            players.append(player)
            player.serial_player()
            players_table.insert(new_player.serialized_player)

    return players

def round_menu_control(tournament, view):

    while True :
        view.tournament_menu_display()
        option_between_round = int(input('Veuillez selectionner un option : '))

        if option_between_round == 1:

            break

        if option_between_round == 2:

            view.player_list_ranking(tournament)

def create_new_tournament(view):

    new_tournament = []
    new_tournament = ControlTournament(view)
    # tournament_player = player_selection_control(full_player_list,view)
    tournament_player = STATIC_LIST_PLAYER
    new_tournament.get_tournament_info(tournament_player)

    new_tournament.round_1('Round 1')
    print(new_tournament.tournament.players)
    round_menu_control(new_tournament.tournament.players,view)
    new_tournament.round_x('Round 2')
    round_menu_control(new_tournament.tournament.players,view)
    new_tournament.round_x('Round 3')
    round_menu_control(new_tournament.tournament.players,view)
    new_tournament.round_x('Round 4')
    new_tournament.tournament.update_score_list()
    view.final_tournament_list_ranking(new_tournament.tournament.players)

    return new_tournament.tournament


view = View()
list_all_tournament: list[Tournament] = []

while True:

    view.start_menu_display()
    option = int(input())

    if option == 1:
        new_tournament = []
        new_tournament = create_new_tournament(view)
        for x in new_tournament.rounds:
            print(x)
        list_player_serialized = new_tournament.list_player_serialization()
        new_tournament.serialize_tournament(list_player_serialized)
        print(new_tournament.serialized_tournament) 
        list_all_tournament.append(new_tournament)
        tournaments_table.insert(new_tournament.serialized_tournament)


    if option == 2:
        player_to_add = view.player_input_view()
        full_player_list.append(player_to_add)
        player_to_add.serial_player()
        players_table.insert(player_to_add.serialized_player)

    if option == 4:
        option_report_chosen = view.report_menu()
        if option_report_chosen == 1:
            view.player_list_ranking_all(full_player_list)
    if option == 5:
        print('Bonne journée !')
        break

    input('Appyuer sur un touche pour retourner au menu principale')
