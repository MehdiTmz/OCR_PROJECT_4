"""Basic view"""
from datetime import datetime
from Include.modele.player import Player
import re

START_MENU_TEXT = {
    'Description': '*********** Bienvenue dans le menu principale *********',
    'Option1': "1 : Créer un tournoi",
    'Option2': "2 : Ajoutez un joueur",
    'Option3': "3 : Changer le rang d'un joueur",
    'Option4': "4 : Liste des rapports",
    'Option5': "5 : Quittez",
    'MessageInput':
    "Veuillez entrer le numéro de l'option que vous désiré choisir :"
}

SUB_MENU_TOURNAMENT_TEXT = {
    'Description': '*********** Menu de tournoi *********',
    'Option 1': '1 : Passer au tour suivant',
    'Option 2': '2 : Afficher la liste des joueurs du tournoi',
    'Option 3': '3 : Changer le rang d''un joueur',
}

SUB_MENU_SELECT_PLAYERS = {
    'Descirption': '*********** Selection des joueurs *********',
    'Option1': '1 : Selectionner un joueur déjà existant',
    'Option2': '2 : Ajouter un nouveau joueur'
}

LIST_PLAYER_TEXT = {
    'Desctiption': 'Voici la liste des joueurs : '
}

LIST_REPORT_TEXT = {
    'Descirption': '*********** Liste des rapports *********',
    'Option1': '1 : Afficher la liste des joueurs',
    'Option2': '2 : Afficher la liste des joueurs d''un trournoi',
    'option3': '3 : Afficher la liste des tournois',
    'option4': '4 : Afficher la listes des rounds d''un tournoi',
    'option5': '5 : Afficher la liste des matchs d''un tournoi'
}


def print_menu(message_dict):
    """Print the message of the menu selected"""
    for k in message_dict.keys():
        print(message_dict[k])


def print_list(list_player):
    """Print a list of player from a tournament player list"""
    for player in list_player:
        print(player[0].name, player[1])


def print_list_full(list_player):
    """Print a list of player from a tournament player list"""
    for player in list_player:
        print('Nom : ' + player.name
              + ' - Prénom : ' + player.firstname
              + '- Rank : ' + str(player.rank))


def print_end_menu():
    """Print end of menus"""
    print('**************************************************')


def control_option_input(size, mesg):
    """Control if the option chosen by the user is valid"""
    number_of_option = []

    while True:
        option_number = int(input(mesg))
        for value in range(1, size+1):
            number_of_option.append(value)
        if option_number in number_of_option:
            return option_number
        else:
            print('Veuillez choisir une option valable !')


def control_word_input(mesg):
    """Control if there is a sepcial character
    or a number in the word entered by the user"""
    SPECIAL_CHARS_LIST = "!@#$%^&*()-+?_=,<>/'"
    DIGIT_LIST = "0123456789"

    while True:
        word = input(mesg)
        if any(character in SPECIAL_CHARS_LIST for character in word):
            pass
        elif any(character in DIGIT_LIST for character in word):
            pass
        else:
            return word
        print("Vous avez utilisé un caractère non valide. Réessayez !")


def control_date_input(mesg):
    """Control the format of the date entered by the user"""
    date_format = "^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$"
    while True:
        date = input(mesg)
        test_date = re.search(date_format, date)
        if test_date:
            return date
        else:
            print('Entrez une date valide !')


def control_rank_number(mesg):
    """Control if the input for the rank is a number"""

    while True:
        rank = input(mesg)

        if rank.isnumeric():
            return rank

        print("Vous avez utilisé un caractère non valide. Réessayez !")


class View:
    """View class

    contain all the view for the application
    """

    def player_input_view(self):
        """ Ask the user the data need to create a player"""

        print('Veuillez entrer les données du joueur : ')
        name = control_word_input('Nom : ')
        firstname = control_word_input('Prénom : ')
        birthdate = control_date_input('Date de naissance : ')
        sex = control_word_input('Sexe : ')
        rank = control_rank_number('Rang : ')
        return Player(name, firstname, birthdate, sex, rank)

    def input_match_result_view(self, player1, player2):
        """Ask the result of a match between 2 player"""

        print('Match : ' + str(player1) + ' contre ' + str(player2))
        text = 'Resultat (1 : joueur 1 gagne, 2 : joueur 2 gagne, un autre nombre si égalité) : '
        result = int(input(text))

        return result

    def start_menu_display(self):

        """Print the start menu"""
        print_menu(START_MENU_TEXT)
        option = int(input())
        print_end_menu()

        return option

    def tournament_menu_display(self):
        """Print the tournament menu"""

        print_menu(SUB_MENU_TOURNAMENT_TEXT)
        print_end_menu()
        output = control_option_input(3, '')

        return output

    def tournament_player_selection_display(self):
        """Print the menu to select
            the player who participate at the tournament"""
        print_menu(SUB_MENU_SELECT_PLAYERS)
        print_end_menu()

    def get_tournament_info(self):
        "Ask the info about the tournament to the user"

        name_tournament = control_word_input('Entrez le nom du tournoi : ')
        place = control_word_input('Entrez l' + ' emplacement du tournoi : ')
        date = datetime.today()
        time_text = 'Entrez le controleur de temps (1 : Blitz, 2 : Bullet, 3 : coup rapide):'
        time_control = input(time_text)
        description = input('Veuillez indiquez vos remarques : ')

        return name_tournament, place, str(date), time_control, description

    def player_list_ranking(self, tournament_list):
        """Print a list of player"""
        print_menu(LIST_PLAYER_TEXT)
        print_list(tournament_list)

    def player_list_ranking_all(self, tournament_list):
        """Print a list of player"""
        print_menu(LIST_PLAYER_TEXT)
        print_list_full(tournament_list)

    def final_tournament_list_ranking(self, tournament_list):
        """Print the winner and the winners of the list"""
        print('*********** Resultats ***********')
        print('Le vainqueur est ' + tournament_list[0][0].name)
        print('Voici la liste finale des joueurs : ')
        for player in tournament_list:
            print(player[0].name, '- score : ', str(player[1]))

    def report_menu(self):
        """Print the menu with all the report available"""
        print_menu(LIST_REPORT_TEXT)
        option = int(input('Veuillez selectionner une option : '))
        return option

    def print_list_tournament_all(self, tournaments_table):
        """Print all the tournament with their name, place and date"""
        for actual_tournament in tournaments_table:
            print(actual_tournament['name'],
                  actual_tournament['place'],
                  actual_tournament['date'])

    def print_rounds(self, tournaments_table):
        """Print all the rounds in a tournament"""
        input_tournament_name = str(input('Nom du tournoi : '))
        for actual_tournament in tournaments_table:
            if actual_tournament['name'] == input_tournament_name:
                count_match = 1
                for key, value in actual_tournament['Rounds'].items():
                    print(key, ' : ')
                    actual_round = actual_tournament['Rounds']['Round' + str(count_match)].items()
                    for key2, value2 in actual_round:
                        print(key2, ' : ', value2)
                    count_match += 1
