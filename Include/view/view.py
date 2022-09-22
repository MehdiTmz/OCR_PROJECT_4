"""Basic view"""
from modele.player import Player

START_MENU_TEXT = {
    'Description': '*********** Bienvenue dans le menu principale *********',
    'Option1' : "1 : Créer un tournoi",
    'Option2' : "2 : Ajoutez un joueur",
    'Option3' : "3 : Changer le rang d'un joueur",
    'Option4' : "4 : Quittez",
    'MessageInput' : "Veuillez entrer le numéro de l'option que vous désiré choisir :"
}

SUB_MENU_TOURNAMENT_TEXT = {
    'Description' : 'Menu de tournoi',
    'Option 1' : '1 : Passer au tour suivant',
    'Option 2' : '2 : Afficher la liste des joueurs du tournoi',
    'Option 3' : '3 : Changer le rang d''un joueur',
}

SUB_MENU_SELECT_PLAYERS = {
    'Descirption' : 'Selection des joueurs',
    'Option1' : '1 : Selectionner un joueur déjà existant',
    'Option2' : '2 : Ajouter un nouveau joueur'
}

LIST_PLAYER_TEXT = {
    'Desctiption' : 'Voici la liste des joueurs : '
}

def print_menu(message_dict):
    """Print the message of the menu selected"""
    for k in message_dict.keys():
        print(message_dict[k])

def print_list(list_player):
    """Print a list of player from a tournament player list"""
    for player in list_player:
        print(player[0].name)

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

    def input_match_result_view(self):
        """Ask the result of a match between 2 player"""
        text = 'Veuillez entre le vainqueur du match (1 = Joueur1, 2 = Joueur2, 0 = Egalité) : '
        result = int(input(text))
        return result

    def start_menu_display(self):
        """Print the start menu"""
        print_menu(START_MENU_TEXT)

    def tournament_menu_display(self):
        """Print the tournament menu"""
        print_menu(SUB_MENU_TOURNAMENT_TEXT)

    def tournament_player_selection_display(self):
        """Print the menu to select the player who participate at the tournament"""
        print_menu(SUB_MENU_SELECT_PLAYERS)

    def get_tournament_info(self):
        "Ask the info about the tournament to the user"
        name_tournament = input('Please enter the name of the tournament')
        return name_tournament

    def player_list_text(self,tournament_list):
        """Print a list of player"""
        print_menu(LIST_PLAYER_TEXT)
        print_list(tournament_list)
