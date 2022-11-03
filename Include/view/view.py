"""Basic view"""
from datetime import datetime
from Include.modele.player import Player
import os


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
    'Option2': "2 : Afficher la liste des joueurs d'un trournoi",
    'option3': '3 : Afficher la liste des tournois',
    'option4': "4 : Afficher la listes des rounds d'un trournoi",
    'option5': "5 : Afficher la liste des matchs d'un trournoi"
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
        print(player)


def print_end_menu():
    """Print end of menus"""
    print('**************************************************')


def control_option_input(size, mesg):
    """Control if the option chosen by the user is valid"""
    number_of_option = []

    while True:
        option_number = int(input(mesg))
        for value in range(1, size + 1):
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
    correct_date = None

    while True:
        date = input(mesg)
        date_test = date.split('/')
        year = date_test[2]
        month = date_test[1]
        day = date_test[0]

        if year.isnumeric() and month.isnumeric() and day.isnumeric():
            if (len(year) == 4 and len(month) == 2 and len(day) == 2):
                try:
                    new_date = datetime.datetime(int(year), int(month), int(day))
                    correct_date = True
                except ValueError:
                    correct_date = False

            if correct_date:
                return new_date

        print("Please enter a valide date")


def control_rank_number(mesg):
    """Control if the input for the rank is a number"""

    while True:
        rank = input(mesg)

        if rank.isnumeric():
            return rank

        print("Vous avez utilisé un caractère non valide. Réessayez !")


def control_sex(mesg):
    """Control the user input for the sex of the player"""

    while True:
        sex = input(mesg)

        if sex in ('M', 'F'):
            return sex

        print("Vous avez utilisé un caractère non valide. Réessayez !")


def control_type_of_tournament(mesg):
    """Controle the user input for the type of tournament"""

    while True:
        type_of_tournament = input(mesg)

        if type_of_tournament in ('1', '2', '3'):
            return type_of_tournament

        print('Veuillez selectionner un option valide.')


class View:
    """View class

    contain all the view for the application
    """

    def player_input_view(self):
        """ Ask the user the data need to create a player"""

        print('Veuillez entrer les données du joueur : ')
        name = control_word_input('Nom : ')
        firstname = control_word_input('Prénom : ')
        birthdate = control_date_input('Date de naissance (JJ/MM/AAAA) : ')
        sex = control_sex('Sexe (M/F) : ')
        rank = control_rank_number('Rang : ')
        return Player(name, firstname, birthdate, sex, rank)

    def input_match_result_view(self, player1, player2):
        """Ask the result of a match between 2 player"""

        print('Match : ' + str(player1) + ' contre ' + str(player2))
        text = ('Resultat' +
                '(1 : joueur 1 gagne,' +
                ' 2 : joueur 2 gagne,' +
                'un autre nombre si égalité) : ')
        result = int(input(text))

        return result

    def start_menu_display(self):
        """Print the start menu"""

        os.system('cls')
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
        time_text = ('Entrez le controleur de temps' +
                     '(1 : Blitz, 2 : Bullet, 3 : coup rapide):')
        time_control = control_type_of_tournament(time_text)
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
                count_round = 1
                for round_number, value in actual_tournament['Rounds'].items():

                    actual_round = actual_tournament['Rounds']['Round' + str(count_round)]
                    print(round_number,
                          '- Debut :', actual_round['date_round_begin'],
                          '- Fin :', actual_round['date_round_begin'],
                          ' : ')

                    for match_number, value2 in actual_round.items():

                        if match_number in ('name',
                                            'date_round_begin',
                                            'date_round_end'):
                            pass

                        else:

                            player1 = actual_round[match_number]['player1']["player"]
                            score1 = actual_round[match_number]['player1']["score"]
                            player2 = actual_round[match_number]['player2']["player"]
                            score2 = actual_round[match_number]['player2']["score"]
                            print('       ',
                                  match_number, ' : ',
                                  player1,
                                  '(score : ', score1, ')',
                                  ' contre ',
                                  player2,
                                  '(score : ', score2, ')',)

                    count_round += 1

    def print_matches(self, tournaments_table):
        """Print all the rounds in a tournament"""
        match_list = []
        input_tournament_name = str(input('Nom du tournoi : '))
        for actual_tournament in tournaments_table:
            if actual_tournament['name'] == input_tournament_name:
                count_round = 1
                for round_number, value in actual_tournament['Rounds'].items():

                    actual_round = actual_tournament['Rounds']['Round' + str(count_round)]
                    print(round_number, actual_round['date_round_begin'], ' : ')

                    for match_number, value2 in actual_round.items():

                        if match_number in ('name',
                                            'date_round_begin',
                                            'date_round_end'):
                            pass

                        else:

                            player1 = actual_round[match_number]['player1']["player"]
                            score1 = actual_round[match_number]['player1']["score"]
                            player2 = actual_round[match_number]['player2']["player"]
                            score2 = actual_round[match_number]['player2']["score"]
                            match_data = [player1, score1, player2, score2]
                            match_list.append(match_data)

                    count_round += 1

        for matches in match_list:
            match_index = match_list.index(matches)
            print('Match' + str(match_index + 1),
                  matches[0],
                  '( score : ' + str(matches[1]) + ')',
                  'contre',
                  matches[2],
                  '( score : ' + str(matches[3]) + ')')

    def print_tournament_player_list(self, tournaments_table):
        """Print list of tournament"""
        input_tournament_name = str(input('Nom du tournoi : '))
        for actual_tournament in tournaments_table:
            if actual_tournament['name'] == input_tournament_name:
                for player in range(0, 8):
                    print(
                        actual_tournament['players'][str(player)]['name'] +
                        ' - Rang : ' +
                        str(actual_tournament['players'][str(player)]['rank']))
