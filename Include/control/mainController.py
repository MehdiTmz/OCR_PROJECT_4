"""Define controller """


from Include.modele.player import Player
from Include.modele.tournament import Tournament
from Include.control.controlTournament import ControlTournament
from Include.view.view import View
from tinydb import TinyDB
from tinydb import where


def player_selection_control(full_player_list, view, players_table):
    """Manage the selection of players for a tournament"""
    players = []

    while len(players) < 8:

        view.tournament_player_selection_display()
        option_player_selection = int(input())

        if option_player_selection == 1:
            player_found = []

            while len(player_found) < 1:
                text = 'Entrez le nom du joueur que vous recherchez : '
                player_name = input(text)
                count = 1
                for player in full_player_list:

                    if player.name == player_name:
                        print(count, ': ' + player.name +
                              ' - ' + player.firstname +
                              ' - ' + player.birthdate +
                              ' - ' + str(player.rank))
                        player_found.append(player)
                        count += 1

                if len(player_found) < 1:
                    print('Aucun joueur trouvé avec ce nom. Réessayez !')

                else:
                    index_player = int(input('Confirmez le joueur : '))

                    if player_found[index_player - 1] in players:
                        print('Ce joueur a déjà été selectionné.')
                    else:
                        players.append(player_found[index_player - 1])

        if option_player_selection == 2:

            new_player = view.player_input_view()
            players.append(new_player)
            full_player_list.append(new_player)
            players_table.insert(new_player.serial_player())

    return players


def player_rank_control(player_list, players_table):
    """Manage the rank update of a player"""

    player_name = input('Entrez le nom du joueur que vous recherchez :')
    player_found = []

    for actual_player in player_list:

        count = 1
        if actual_player.name == player_name:
            print(count, ': ' + actual_player.name +
                  ' - ' + actual_player.firstname +
                  ' - ' + actual_player.birthdate +
                  ' - ' + str(actual_player.rank))
            player_found.append(actual_player)
            count += 1
        else:
            print('Aucun joueur trouvé')

    index_player = int(input('Confirmez le joueur : '))
    name = player_found[index_player - 1].name
    firstname = player_found[index_player - 1].firstname

    for actual_player_in_list in player_list:
        if(name == actual_player_in_list.name and firstname == actual_player_in_list.firstname):

            new_rank_txt = 'Veuillez entrez le nouveau rang du joueur'
            actual_player_in_list.rank = int(input(new_rank_txt))
            players_table.update({'rank': actual_player_in_list.rank},
                                 (where('name') == name) & (where('firstname') == firstname))
    return player_list


def create_database_player(database):
    """Create player database
    and manage the full player list if the database exist"""

    full_player_list = []
    if database.table('player'):
        players_table = database.table('player')
        for player in players_table:
            player_to_add = Player(player['name'], player['firstname'],
                                   player['birthdate'], player['sex'],
                                   player['rank'])
            full_player_list.append(player_to_add)
    else:
        players_table = database.table('player')
    return full_player_list


class mainController:
    """Main controller class
        has one attribute"""

    view: View()
    full_player_list: list[Player] = []
    list_all_tournament: list[Tournament] = []
    db = TinyDB('data\db.json')
    players_table = db.table("player")
    tournaments_table = db.table('tournament')
    full_player_list = create_database_player(db)

    def __init__(self, control_view):
        """Constructor"""
        self.view = control_view

    def round_menu_control(self, tournament, players_table):
        """Mange the menu between rounds"""

        while True:

            option_between_round = self.view.tournament_menu_display()

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
        new_tournament = ControlTournament(self.view)
        tournament_player = player_selection_control(
            self.full_player_list,
            self.view,
            self.players_table)
        # tournament_player = STATIC_LIST_PLAYER
        new_tournament.get_tournament_info(tournament_player)
        # print(new_tournament.tournament.players)
        new_tournament.round_1('Round 1')
        self.round_menu_control(
            new_tournament.tournament.players,
            self.players_table)
        new_tournament.round_x('Round 2')
        self.round_menu_control(
            new_tournament.tournament.players,
            self.players_table)
        new_tournament.round_x('Round 3')
        self.round_menu_control(
            new_tournament.tournament.players,
            self.players_table)
        new_tournament.round_x('Round 4')
        new_tournament.tournament.update_score_list()
        self.view.final_tournament_list_ranking(
            new_tournament.tournament.players)

        return new_tournament.tournament

    def run(self):
        """run the main meny"""
        while True:

            option = self.view.start_menu_display()

            if option == 1:
                new_tournament = []
                new_tournament = self.create_new_tournament()
                list_serialized = new_tournament.list_player_serialization()
                # list_all_tournament.append(new_tournament)
                tournament_add = new_tournament.serialize_tournament(
                    list_serialized)
                self.tournaments_table.insert(tournament_add)

            if option == 2:
                player_to_add = self.view.player_input_view()
                self.full_player_list.append(player_to_add)
                self.players_table.insert(player_to_add.serial_player())

            if option == 3:
                self.full_player_list = player_rank_control(
                    self.full_player_list,
                    self.players_table)

            if option == 4:

                option_report_chosen = self.view.report_menu()

                if option_report_chosen == 1:
                    self.view.player_list_ranking_all(self.full_player_list)

                if option_report_chosen == 2:
                    self.view.print_tournament_player_list(
                        self.tournaments_table)

                if option_report_chosen == 3:
                    self.view.print_list_tournament_all(self.tournaments_table)

                if option_report_chosen == 4:
                    self.view.print_rounds(self.tournaments_table)

                if option_report_chosen == 5:
                    self.view.print_matches(self.tournaments_table)

            if option == 5:
                print('Bonne journée !')
                break

            input('Appyuer sur un touche pour retourner au menu principale')
