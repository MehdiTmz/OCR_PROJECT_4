"""Define tournament controler"""
# from Include.modele.match import Match
# from Include.modele.round import Round
# from datetime import datetime
from Include.modele.player import Player
from Include.modele.tournament import Tournament
from controlTournament import ControlTournament
from Include.view.view import View
from tinydb import TinyDB
from tinydb import where
# import random

db = TinyDB('db.json')
full_player_list: list[Player] = []

if db.table('player'):
    players_table = db.table('player')
    for player in players_table:
        player_to_add = Player(player['name'], player['firstname'],
                               player['birthdate'], player['sex'],
                               player['rank'])
        full_player_list.append(player_to_add)
else:
    players_table = db.table('player')

if db.table('tournament'):
    tournaments_table = db.table('tournament')
else:
    tournaments_table = db.table('tournament')


def player_selection_control(full_player_list, view):
    """Manage the selection of players for a tournament"""
    players = []

    while len(players) < 8:

        view.tournament_player_selection_display()
        option_player_selection = int(input())

        if option_player_selection == 1:

            text = 'Entrez le nom du joueur que vous recherchez :'
            player_name = input(text)
            player_found = []

            for player in full_player_list:
                count = 1
                if player.name == player_name:
                    print(count, ': ' + player.name
                          + ' - ' + player.firstname
                          + ' - ' + player.birthdate + ' - '
                          + str(player.rank))
                    player_found.append(player)
                    count += 1
                else:
                    print('Aucun joueur trouvé')

            index_player = int(input('Confirmez le joueur : '))
            players.append(player_found[index_player - 1])

        if option_player_selection == 2:

            new_player = view.player_input_view()
            players.append(new_player)
            players_table.insert(new_player.serial_player())

    return players


def player_rank_control(player_list, players_table):
    """Manage the rank update of a player"""

    player_name = input('Entrez le nom du joueur que vous recherchez :')
    player_found = []

    for actual_player in player_list:

        count = 1
        if actual_player.name == player_name:
            print(count, ': ' + actual_player.name
                  + ' - ' + actual_player.firstname
                  + ' - ' + actual_player.birthdate + ' - '
                  + str(actual_player.rank))
            player_found.append(actual_player)
            count += 1
        else:
            print('Aucun joueur trouvé')

    index_player = int(input('Confirmez le joueur : '))
    name = player_found[index_player - 1].name
    firstname = player_found[index_player - 1].firstname

    for actual_player_in_list in player_list:
        if(name == actual_player_in_list.name
                and firstname == actual_player_in_list.firstname):

            new_rank_txt = 'Veuillez entrez le nouveau rang du joueur'
            actual_player_in_list.rank = int(input(new_rank_txt))
            players_table.update({'rank': actual_player_in_list.rank},
                                 (where('name') == name)
                                 & (where('firstname') == firstname))
    return player_list


def round_menu_control(tournament, view, players_table):
    """Mange the menu between rounds"""

    while True:

        option_between_round = view.tournament_menu_display()

        if option_between_round == 1:

            break

        if option_between_round == 2:

            view.player_list_ranking(tournament)

        if option_between_round == 3:
            player_list = [player[0] for player in tournament]
            player_rank_control(player_list, players_table)


def create_new_tournament(view):
    """Create a new tournament"""

    new_tournament = []
    new_tournament = ControlTournament(view)
    tournament_player = player_selection_control(full_player_list,view)
    # tournament_player = STATIC_LIST_PLAYER
    new_tournament.get_tournament_info(tournament_player)
    # print(new_tournament.tournament.players)
    new_tournament.round_1('Round 1')
    round_menu_control(new_tournament.tournament.players, view, players_table)
    new_tournament.round_x('Round 2')
    round_menu_control(new_tournament.tournament.players, view, players_table)
    new_tournament.round_x('Round 3')
    round_menu_control(new_tournament.tournament.players, view, players_table)
    new_tournament.round_x('Round 4')
    new_tournament.tournament.update_score_list()
    view.final_tournament_list_ranking(new_tournament.tournament.players)

    return new_tournament.tournament


view = View()
list_all_tournament: list[Tournament] = []

while True:

    option = view.start_menu_display()

    if option == 1:
        new_tournament = []
        new_tournament = create_new_tournament(view)
        list_serialized = new_tournament.list_player_serialization()
        list_all_tournament.append(new_tournament)
        tournament_add = new_tournament.serialize_tournament(list_serialized)
        tournaments_table.insert(tournament_add)

    if option == 2:
        player_to_add = view.player_input_view()
        full_player_list.append(player_to_add)
        players_table.insert(player_to_add.serial_player())

    if option == 3:
        full_player_list = player_rank_control(full_player_list, players_table)

    if option == 4:
        option_report_chosen = view.report_menu()
        if option_report_chosen == 1:
            view.player_list_ranking_all(full_player_list)
        if option_report_chosen == 2:
            input_tournament_name = str(input('Nom du tournoi : '))
            for actual_tournament in tournaments_table:
                if actual_tournament['name'] == input_tournament_name:
                    for player in range(0, 8):
                        print(actual_tournament['players'][str(player)]['name']
                              + ' - Rang : '
                              + str(actual_tournament['players'][str(player)]['rank']))
        if option_report_chosen == 3:
            view.print_list_tournament_all(tournaments_table)
        if option_report_chosen == 4:
            view.print_rounds(tournaments_table)

    if option == 5:
        print('Bonne journée !')
        break

    input('Appyuer sur un touche pour retourner au menu principale')

class mainController:
    """Main controller class
        has one attribute"""

    view : view()
    full_player_list: list[Player] = []
    list_all_tournament: list[Tournament] = []
    db = TinyDB('db.json')

    if db.table('player'):
        players_table = db.table('player')
        for player in players_table:
            player_to_add = Player(player['name'], player['firstname'],
                                player['birthdate'], player['sex'],
                                player['rank'])
            full_player_list.append(player_to_add)
    else:
        players_table = db.table('player')

    if db.table('tournament'):
        tournaments_table = db.table('tournament')
    else:
        tournaments_table = db.table('tournament')

    def __init__(self,control_view):
        """Constructor"""
        self.view = control_view

    def round_menu_control(self, tournament, players_table):
        """Mange the menu between rounds"""

        while True:

            option_between_round = view.tournament_menu_display()

            if option_between_round == 1:

                break

            if option_between_round == 2:

                self.view.player_list_ranking(tournament)

            if option_between_round == 3:

                player_list = [player[0] for player in tournament]
                player_rank_control(player_list, players_table)

    def create_new_tournament(self):
        """Create a new tournament"""

        new_tournament = []
        new_tournament = ControlTournament(view)
        tournament_player = player_selection_control(full_player_list,view)
        # tournament_player = STATIC_LIST_PLAYER
        new_tournament.get_tournament_info(tournament_player)
        # print(new_tournament.tournament.players)
        new_tournament.round_1('Round 1')
        self.round_menu_control(new_tournament.tournament.players, players_table)
        new_tournament.round_x('Round 2')
        self.round_menu_control(new_tournament.tournament.players, players_table)
        new_tournament.round_x('Round 3')
        self.round_menu_control(new_tournament.tournament.players, players_table)
        new_tournament.round_x('Round 4')
        new_tournament.tournament.update_score_list()
        self.view.final_tournament_list_ranking(new_tournament.tournament.players)

        return new_tournament.tournament

    def run(self):
        """run the main meny"""
        while True:

            option = view.start_menu_display()

            if option == 1:
                new_tournament = []
                new_tournament = create_new_tournament(view)
                list_serialized = new_tournament.list_player_serialization()
                list_all_tournament.append(new_tournament)
                tournament_add = new_tournament.serialize_tournament(list_serialized)
                tournaments_table.insert(tournament_add)

            if option == 2:
                player_to_add = view.player_input_view()
                self.full_player_list.append(player_to_add)
                players_table.insert(player_to_add.serial_player())

            if option == 3:
                self.full_player_list = player_rank_control(full_player_list, players_table)

            if option == 4:

                option_report_chosen = view.report_menu()

                if option_report_chosen == 1:
                    view.player_list_ranking_all(full_player_list)

                if option_report_chosen == 2:
                    input_tournament_name = str(input('Nom du tournoi : '))
                    for actual_tournament in tournaments_table:
                        if actual_tournament['name'] == input_tournament_name:
                            for player in range(0, 8):
                                print(actual_tournament['players'][str(player)]['name']
                                        + ' - Rang : '
                                        + str(actual_tournament['players'][str(player)]['rank']))

                if option_report_chosen == 3:
                    view.print_list_tournament_all(tournaments_table)

                if option_report_chosen == 4:
                    view.print_rounds(tournaments_table)

            if option == 5:
                print('Bonne journée !')
                break

            input('Appyuer sur un touche pour retourner au menu principale')
