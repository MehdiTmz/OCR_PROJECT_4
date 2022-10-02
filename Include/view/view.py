"""Basic view"""
from datetime import datetime
from Include.modele.player import Player

START_MENU_TEXT = {
    'Description': '*********** Bienvenue dans le menu principale *********',
    'Option1' : "1 : Créer un tournoi",
    'Option2' : "2 : Ajoutez un joueur",
    'Option3' : "3 : Changer le rang d'un joueur",
    'Option4' : "4 : Liste des rapports",
    'Option5' : "5 : Quittez",
    'MessageInput' : "Veuillez entrer le numéro de l'option que vous désiré choisir :"
}

SUB_MENU_TOURNAMENT_TEXT = {
    'Description' : '*********** Menu de tournoi *********',
    'Option 1' : '1 : Passer au tour suivant',
    'Option 2' : '2 : Afficher la liste des joueurs du tournoi',
    'Option 3' : '3 : Changer le rang d''un joueur',
}

SUB_MENU_SELECT_PLAYERS = {
    'Descirption' : '*********** Selection des joueurs *********',
    'Option1' : '1 : Selectionner un joueur déjà existant',
    'Option2' : '2 : Ajouter un nouveau joueur'
}

LIST_PLAYER_TEXT = {
    'Desctiption' : 'Voici la liste des joueurs : '
}
LIST_REPORT_TEXT = {
    'Descirption' : '*********** Liste des rapports *********',
    'Option1' : '1 : Afficher la liste des joueurs',
    'Option2' : '2 : Afficher la liste des joueurs d''un trournoi',
    'option3' : '3 : Afficher la liste des tournois',
    'option4' : '4 : Afficher la listes des rounds d''un tournoi',
    'option5' : '5 : Afficher la liste des matchs d''un tournoi'
}
def print_menu(message_dict):
    """Print the message of the menu selected"""
    for k in message_dict.keys():
        print(message_dict[k])

def print_list(list_player):
    """Print a list of player from a tournament player list"""
    for player in list_player:
        print(player[0].name)

def print_list_full(list_player):
    """Print a list of player from a tournament player list"""
    for player in list_player:
        print('Nom : ' + player.name +' - Prénom : ' + player.firstname + '- Rank : ' + str(player.rank))

def print_end_menu():
    """Print end of menus"""
    print('**************************************************')

class View :
    """View class

    contain all the view for the application
    """

    def player_input_view(self):
        """ Ask the user the data need to create a player"""
        print('Veuillez entrer les données du joueur : ')
        name = input('Nom : ')
        firstname = input('Prénom : ')
        birthdate = input('Date de naissance : ')
        sex = input('Sexe : ')
        rank = int(input('Rang : '))
        return Player(name,firstname,birthdate,sex,rank)

    def input_match_result_view(self,player1,player2):
        """Ask the result of a match between 2 player"""
        print('Match : ' + str(player1) + ' contre ' + str(player2))
        text ='Resultat (1 : joueur 1 gagne, 2 : joueur 2 gagne, un autre nombre si égalité) : '
        result = int(input(text))
        return result

    def start_menu_display(self):
        """Print the start menu"""
        print_menu(START_MENU_TEXT)
        print_end_menu()

    def tournament_menu_display(self):
        """Print the tournament menu"""
        print_menu(SUB_MENU_TOURNAMENT_TEXT)
        print_end_menu()
        output = int(input('Veuillez selectionner un option : '))
        return output

    def tournament_player_selection_display(self):
        """Print the menu to select the player who participate at the tournament"""
        print_menu(SUB_MENU_SELECT_PLAYERS)
        print_end_menu()

    def get_tournament_info(self):
        "Ask the info about the tournament to the user"
        name_tournament = input('Entrez le nom du tournoi : ')
        place = input('Entrez l' + ' emplacement du tournoi : ')
        #date = datetime.today()
        time_text = 'Entrez le controleur de temps (1 : Blitz, 2 : Bullet, 3 : coup rapide):'
        time_control = input(time_text)
        description = input('Veuillez indiquez vos remarques : ')
        return name_tournament,place,time_control,description

    def player_list_ranking(self,tournament_list):
        """Print a list of player"""
        print_menu(LIST_PLAYER_TEXT)
        print_list(tournament_list)

    def player_list_ranking_all(self,tournament_list):
        """Print a list of player"""
        print_menu(LIST_PLAYER_TEXT)
        print_list_full(tournament_list)

    def final_tournament_list_ranking(self,tournament_list):
        """Print the winner and the winners of the list"""
        print('*********** Resultats ***********')
        print('Le vainqueur est ' + tournament_list[0][0].name)
        print('Voici la liste finale des joueurs : ')
        for player in tournament_list:
            print(player[0].name, '- score : ', str(player[1]))

    def report_menu(self):
        print_menu(LIST_REPORT_TEXT)
        option = int(input('Veuillez selectionner une option : '))
        return option
    def print_list_tournament_all(self,tournaments_table):
        "Print all the tournament with their name, place and date"
        for actual_tournament in tournaments_table:
            print(actual_tournament['name'],actual_tournament['place'],actual_tournament['date'])
